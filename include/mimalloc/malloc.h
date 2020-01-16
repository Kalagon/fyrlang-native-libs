#include <stdint.h>

uint8_t* mi_malloc(uint64_t size);
void mi_free(uint8_t* ptr);
uint8_t* mi_calloc(uint64_t nmemb, uint64_t size);
void *mi_realloc(void *ptr, uint64_t size);

