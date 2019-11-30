# Contributing

## Build Scripts

The build scripts reside in the `scripts` directory.
They perform all necessary tasks to fetch, compile, and move the library archive to the `lib` folder.
Compilation is done inside the `src` folder.

They should accept at least three arguments, in this order:

- `SRC_PATH` The path to the `src` folder.
- `LIB_PATH` The path to the `lib` folder.
- `MAKE` The `make` executable that was used to invoke the Makefile.

The scripts compile the libraries for the host platform.
Please ensure that the compiled libraries are statically linkable.

The library folders in `lib` __must__ provide an `INFO` file with a short description and links to the source, and all files required for distribution in binary form.
This usually encompasses the license file of the source repository.

## Code of Conduct

Be nice and respectful and stay on topic.
While we understand, that discussions might get heated sometimes, personal attacks will not be tolerated.

TODO
