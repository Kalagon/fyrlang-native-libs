import os
import sys
import urllib.request
import tarfile
import subprocess

VERSION = "5.2.1"
SOURCE = "https://github.com/jemalloc/jemalloc/releases/download/{version}/jemalloc-{version}.tar.bz2".format(version=VERSION)

SRC_PATH = sys.argv[1]
LIB_PATH = sys.argv[2]
MAKE = sys.argv[3]

def get_source():
	with urllib.request.urlopen(SOURCE) as response:
		with tarfile.open(fileobj=response, mode="r|bz2") as tar:
			tar.extractall(path=SRC_PATH)

def prepare():
	configureScript = ['./configure']
	configureArgs = ['--enable-static', '--without-export', '--disable-cxx', '--disable-libdl', '--disable-prof-gcc', '--disable-prof-libgcc', '--disable-stats', '--with-jemalloc-prefix=je_']
	srcDir = "{src}/jemalloc-{version}".format(src=SRC_PATH, version=VERSION)
	subprocess.run(configureScript + configureArgs, cwd=srcDir, stdout=sys.stdout, stderr=sys.stderr)

def build():
	srcDir = "{src}/jemalloc-{version}".format(src=SRC_PATH, version=VERSION)
	subprocess.run([MAKE, 'build_lib_static'], cwd=srcDir, stdout=sys.stdout, stderr=sys.stderr)

def move_artifact():
	libFile = "{src}/jemalloc-{version}/lib/libjemalloc.a".format(src=SRC_PATH, version=VERSION)
	uname = os.uname()
	targetDir = "{lib}/jemalloc/{platform}-{machine}/".format(lib=LIB_PATH, platform=str.lower(uname.sysname), machine=str.lower(uname.machine))
	os.makedirs(targetDir, mode=0o755, exist_ok=True)
	os.rename(libFile, targetDir + 'libjemalloc.a')

get_source()
prepare()
build()
move_artifact()
