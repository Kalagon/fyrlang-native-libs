#include <stdint.h>

uint8_t* rpmalloc(uint64_t size);
void rpfree(uint8_t* ptr);
uint8_t* rpcalloc(uint64_t nmemb, uint64_t size);
void *rprealloc(void *ptr, uint64_t size);

