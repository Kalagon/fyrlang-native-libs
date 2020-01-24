# Fyrlang Native Libraries

This repository contains the scripts used to precompile native libraries used by the Fyrlang compiler.

## Building

For each library there is a `make` target.
To build a library, simply run `make <library>`.

Running `make` without arguments will build all supported libraries

### Libraries

These libraries are currently supported:

- `jemalloc`: The [jemalloc](https://github.com/jemalloc/jemalloc) memory allocator, originally written for FreeBSD
- `tcmalloc`: Memory allocator included in [gperftools](https://github.com/gperftools/gperftools) by Google
- `mimalloc`: [mimalloc](https://github.com/microsoft/mimalloc) by Daan Leijen and Microsoft
- `rpmalloc`: [rpmalloc](https://github.com/mjansson/rpmalloc) by Mattias Jansson

### Requirements

The scripts in this repository only need `make` and `python3`.
Your system needs to also provide the required utilities for the libraries to succeed.

Please be aware that this list might change and is not guaranteed to be exhaustive:
- _jemalloc_: `gcc`
- _tcmalloc_: `g++`
- _mimalloc_: `gcc`, `cmake`
- _rpmalloc_: `clang`, `ninja`

## Updating

As long as the build process for a library does not change, updating it is as simple as editing the `VERSION` variable in its corresponding script.

## License

The script files in this repository are provided with the included [license](LICENSE.md).
The compiled libraries are subject to the licenses in their respective folders.

