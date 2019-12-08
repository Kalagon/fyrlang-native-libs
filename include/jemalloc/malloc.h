#include <stdint.h>

uint8_t* je_malloc(uint64_t size);
void je_free(uint8_t* ptr);
uint8_t* je_calloc(uint64_t nmemb, uint64_t size);
void *je_realloc(void *ptr, uint64_t size);

