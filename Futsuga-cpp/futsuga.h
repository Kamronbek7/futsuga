#include <stdio.h>
// #include "cJSON.h"
#include "read_json.h"
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <curl/curl.h>
#include <futs_string.h>

// CURL *curl;
// CURLcode res;

typedef struct {
    char *data;
    size_t size;
} Memory;

// Bot structure
typedef struct {
    char * TOKEN;
} Bot;

// Rework the replied data
typedef struct {
    char * reply_data;
} ReplyData;

size_t write_cb(void *contents, size_t size, size_t nmemb, void *userp) {
    size_t realsize = size * nmemb;
    Memory *mem = (Memory *)userp;

    char *ptr = realloc(mem->data, mem->size + realsize + 1);
    if (!ptr) return 0;

    mem->data = ptr;
    memcpy(&(mem->data[mem->size]), contents, realsize);
    mem->size += realsize;
    mem->data[mem->size] = 0;
    return realsize;
}

typedef struct {
    char url[512];
    void (*callback)(const char *result);
} AsyncRequest;

DWORD WINAPI async_thread(LPVOID param) {//, CURL *curl, CURLcode res) {
    CURL *curl;
    CURLcode res;
    
    AsyncRequest *req = (AsyncRequest *)param;
    Memory chunk = { malloc(1), 0 };

    curl = curl_easy_init();
    if (!curl) {
        req->callback("curl init error");
        free(req);
        return 0;
    }

    curl_easy_setopt(curl, CURLOPT_CAINFO, "cacert.crt");
    curl_easy_setopt(curl, CURLOPT_URL, req->url);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_cb);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &chunk);

    // SSL verifikatsiyani yoqish/oo‘rnatish
    curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0L);
    curl_easy_setopt(curl, CURLOPT_SSL_VERIFYHOST, 0L);

    res = curl_easy_perform(curl);

    char *out;
    if (res != CURLE_OK) {
        out = strdup(curl_easy_strerror(res));
    } else {
        out = strdup(chunk.data);
    }

    // curl_easy_cleanup(curl);
    free(chunk.data);

    req->callback(out);
    free(out);
    free(req);

    return 0;
}

void send_async_request(const char *url, void (*callback)(const char *result)) {
    AsyncRequest *r = malloc(sizeof(AsyncRequest));
    strcpy(r->url, url);
    r->callback = callback;

    CreateThread(NULL, 0, async_thread, r, 0, NULL);
}

json send_request(const char *url) {
    CURL *curl;
    CURLcode res;
    Memory chunk = { malloc(1), 0 };

    curl = curl_easy_init();
    if (!curl) {
        fprintf(stderr, "Curl init error\n");
        exit(1);
    }

    curl_easy_setopt(curl, CURLOPT_CAINFO, "cacert.crt");
    curl_easy_setopt(curl, CURLOPT_URL, url);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_cb);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &chunk);

    // SSL verifikatsiyani yoqish/oo‘rnatish
    curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0L);
    curl_easy_setopt(curl, CURLOPT_SSL_VERIFYHOST, 0L);

    res = curl_easy_perform(curl);

    if (res != CURLE_OK) {
        fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
        exit(1);
    }

    curl_easy_cleanup(curl);

    json j = { cJSON_Parse(chunk.data) };
    free(chunk.data);
    return j;
}

str TG_URL = { "https://api.telegram.org/bot", 28 };

int run_bot(Bot bot) {
    if (bot.TOKEN == NULL) return 502;
    else {
        str token = { bot.TOKEN, 46 };
        bool ok;
        str boturl, desc;
        {
            boturl = str___add(TG_URL, token);
            str getme = { "/getMe", 6 };
            str url = str___add(boturl, getme);

            json data = send_request(url.data);

            ok = get_element_bool(&data, "ok");
            if (!ok) {
                desc.data = get_element_str(&data, "description");
                desc.length = strlen(desc.data);
            }
        }

        if (ok) {
            printf("Bot is running...\n");
            while (1) {
            }
        } else {
            printf("%s\n", desc.data);
        }
    }
    return 0;
}