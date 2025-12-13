// safe_input.c  -- kompilyatsiya: tcc safe_input.c -o safe_input
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <errno.h>

#define INITIAL_CAP 128
#define MAX_LIMIT (1 << 20) // 1 MB, kerak bo'lsa oshir

// Oddiy UTF-8 validator: true agar buf[0..len) haqiqiy UTF-8 bo'lsa
int utf8_validate(const unsigned char *s, size_t len) {
    size_t i = 0;
    while (i < len) {
        unsigned char c = s[i];
        if (c < 0x80) { i++; continue; }         // ASCII
        else if ((c >> 5) == 0x6) {              // 110x xxxx  - 2 bytes
            if (i + 1 >= len) return 0;
            if ((s[i+1] >> 6) != 0x2) return 0;
            if ((c & 0x1E) == 0) return 0; // overlong
            i += 2;
        } else if ((c >> 4) == 0xE) {           // 1110 xxxx - 3 bytes
            if (i + 2 >= len) return 0;
            if ((s[i+1] >> 6) != 0x2 || (s[i+2] >> 6) != 0x2) return 0;
            i += 3;
        } else if ((c >> 3) == 0x1E) {          // 1111 0xxx - 4 bytes
            if (i + 3 >= len) return 0;
            if ((s[i+1] >> 6) != 0x2 || (s[i+2] >> 6) != 0x2 || (s[i+3] >> 6) != 0x2) return 0;
            i += 4;
        } else return 0;
    }
    return 1;
}

// Filtrlash: control characterlarni tozalash (faqat TAB va newline ruxsat etiladi)
void sanitize_inplace(unsigned char *s, size_t len) {
    for (size_t i = 0; i < len; ++i) {
        unsigned char c = s[i];
        if (c == '\t' || c == '\n' || (c >= 0x20 && c <= 0x7E)) continue;
        // agar UTF-8 extension qismida bo'lsa, qoldiramiz (ya'ni yuqorida validaqiya qilingan)
        // oddiy control charlarni ? bilan almashtiramiz
        if (c < 0x20) s[i] = '?';
    }
}

// Safe readline: return malloc'ed buffer (null-terminated) and set *out_len.
// Caller responsible for free(). On error returns NULL.
char* input(size_t max_limit, size_t *out_len) {
    if (max_limit == 0 || max_limit > MAX_LIMIT) max_limit = MAX_LIMIT;

    size_t cap = INITIAL_CAP;
    char *buf = (char*)malloc(cap);
    if (!buf) return NULL;

    size_t len = 0;
    int ch;
    while ((ch = getchar()) != EOF) {
        if (ch == '\r') continue; // Windows \r ignore
        if (ch == '\n') {
            break;
        }

        // grow if needed
        if (len + 1 >= cap) {
            size_t newcap = cap * 2;
            if (newcap > max_limit) newcap = max_limit;
            if (len + 1 >= newcap) { // limit reached
                // read and discard rest of line
                while ((ch = getchar()) != EOF && ch != '\n') {}
                buf[len] = '\0';
                *out_len = len;
                sanitize_inplace((unsigned char*)buf, len);
                return buf;
            }
            char *tmp = (char*)realloc(buf, newcap);
            if (!tmp) { free(buf); return NULL; }
            buf = tmp;
            cap = newcap;
        }
        buf[len++] = (char)ch;
    }

    // if EOF and nothing read -> return NULL (or empty string based on policy)
    if (len == 0 && ch == EOF) { free(buf); return NULL; }

    buf[len] = '\0';

    // UTF-8 validate: agar noto'g'ri bo'lsa, bu yerda hal qilish mumkin:
    if (!utf8_validate((unsigned char*)buf, len)) {
        // variantlar: qayta-encode, replace with '?', yoki xatolik qaytar
        // biz bu misolda simple sanitizatsiya qilamiz
        for (size_t i = 0; i < len; ++i)
            if ((unsigned char)buf[i] < 0x20) buf[i] = '?';
    }

    sanitize_inplace((unsigned char*)buf, len);

    *out_len = len;
    return buf;
}

/* Misol foydalanish */
/*int main(void) {
    printf("Enter something (max 1MB): ");
    size_t len;
    char *s = input(1024*1024, &len);
    if (!s) {
        printf("No input or error\n");
        return 1;
    }

    // Xavfsiz chop etish: length ni aniq beramiz
    printf("You typed (len=%zu): ", len);
    printf("%.*s\n", (int)len, s);

    free(s);
    return 0;
}*/