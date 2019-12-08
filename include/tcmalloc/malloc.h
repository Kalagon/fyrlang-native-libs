#include <stdint.h>

uint8_t* tc_malloc(uint64_t size);
void tc_free(uint8_t* ptr);
uint8_t* tc_calloc(uint64_t nmemb, uint64_t size);
void *tc_realloc(void *ptr, uint64_t size);

