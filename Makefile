SRC_PATH=$(CURDIR)/src
LIB_PATH=$(CURDIR)/lib
LIBRARIES= jemalloc tcmalloc mimalloc

.PHONY: all
all: $(LIBRARIES)

.PHONY: clean
clean:
	rm -rf src/*
	find ./lib -name '*.a' -exec rm -rf {} +

.PHONY: $(LIBRARIES)
$(LIBRARIES):
	python3 scripts/$@.py $(SRC_PATH) $(LIB_PATH) $(MAKE)
