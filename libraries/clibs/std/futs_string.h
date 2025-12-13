#include <stdio.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *data;
    size_t length;
} str;

str str___add(str a, str b) {
    str result;
    result.length = a.length + b.length;

    result.data = malloc(result.length + 1);
    if (!result.data) {
        result.length = 0;
        return result; 
    }

    memcpy(result.data, a.data, a.length);
    memcpy(result.data + a.length, b.data, b.length);

    result.data[result.length] = '\0';

    return result;
}
