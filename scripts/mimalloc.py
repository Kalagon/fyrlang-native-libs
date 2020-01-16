import os
import sys
import urllib.request
import tarfile
import subprocess

VERSION = "1.2.2"
SOURCE = "https://github.com/microsoft/mimalloc/archive/v{version}.tar.gz".format(version=VERSION)

SRC_PATH = sys.argv[1]
LIB_PATH = sys.argv[2]
MAKE = sys.argv[3]

def get_source():
	with urllib.request.urlopen(SOURCE) as response:
		with tarfile.open(fileobj=response, mode="r|gz") as tar:
			tar.extractall(path=SRC_PATH)

def prepare():
	configureScript = ['cmake']
	configureArgs = ['../..']
	srcDir = "{src}/mimalloc-{version}/out/release".format(src=SRC_PATH, version=VERSION)
	os.makedirs(srcDir, mode=0o755, exist_ok=True)
	subprocess.run(configureScript + configureArgs, cwd=srcDir, stdout=sys.stdout, stderr=sys.stderr)

def build():
	srcDir = "{src}/mimalloc-{version}/out/release".format(src=SRC_PATH, version=VERSION)
	subprocess.run([MAKE], cwd=srcDir, stdout=sys.stdout, stderr=sys.stderr)

def move_artifact():
	libFile = "{src}/mimalloc-{version}/out/release/libmimalloc.a".format(src=SRC_PATH, version=VERSION)
	uname = os.uname()
	targetDir = "{lib}/mimalloc/{platform}-{machine}/".format(lib=LIB_PATH, platform=str.lower(uname.sysname), machine=str.lower(uname.machine))
	os.makedirs(targetDir, mode=0o755, exist_ok=True)
	os.rename(libFile, targetDir + 'libmimalloc.a')

get_source()
prepare()
build()
move_artifact()
