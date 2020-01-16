import os
import sys
import urllib.request
import tarfile
import subprocess
import re

VERSION = "1.4.0"
SOURCE = "https://github.com/mjansson/rpmalloc/archive/{version}.tar.gz".format(version=VERSION)

SRC_PATH = sys.argv[1]
LIB_PATH = sys.argv[2]
MAKE = sys.argv[3]

def get_source():
	with urllib.request.urlopen(SOURCE) as response:
		with tarfile.open(fileobj=response, mode="r|gz") as tar:
			tar.extractall(path=SRC_PATH)

def prepare():
	configureScript = ['./configure.py']
	srcDir = "{src}/rpmalloc-{version}".format(src=SRC_PATH, version=VERSION)
	subprocess.run(configureScript, cwd=srcDir, stdout=sys.stdout, stderr=sys.stderr)

def build():
	srcDir = "{src}/rpmalloc-{version}".format(src=SRC_PATH, version=VERSION)
	subprocess.run(["ninja"], cwd=srcDir, stdout=sys.stdout, stderr=sys.stderr)

def move_artifact():
	for root, _, files in os.walk("{src}/rpmalloc-{version}/lib/".format(src=SRC_PATH, version=VERSION)):
		if not re.match(r".*/rpmalloc-.*/lib/.*/release/.*", root):
			continue
		for file in files:
			if file == "librpmalloc.a":
				libFile = root + "/" + file
				break
	uname = os.uname()
	targetDir = "{lib}/rpmalloc/{platform}-{machine}/".format(lib=LIB_PATH, platform=str.lower(uname.sysname), machine=str.lower(uname.machine))
	os.makedirs(targetDir, mode=0o755, exist_ok=True)
	os.rename(libFile, targetDir + 'librpmalloc.a')

get_source()
prepare()
build()
move_artifact()
