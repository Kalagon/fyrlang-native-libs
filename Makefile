SRC_PATH=$(CURDIR)/src
LIB_PATH=$(CURDIR)/lib

.PHONY: all
all: jemalloc tcmalloc

.PHONY: clean
clean:
	rm -rf src/*

.PHONY: jemalloc
jemalloc:
	python3 scripts/jemalloc.py $(SRC_PATH) $(LIB_PATH) $(MAKE)

.PHONY: tcmalloc
tcmalloc:
	python3 scripts/tcmalloc.py $(SRC_PATH) $(LIB_PATH) $(MAKE)

