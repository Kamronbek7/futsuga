#include <stdio.h>
#include <stdlib.h>
#include <cJSON.c>

typedef struct {
    cJSON *json;
} json;

char * get_element_str(json *j, const char *key) {
    cJSON *city_item = cJSON_GetObjectItemCaseSensitive(j->json, key);
    if (cJSON_IsString(city_item) && (city_item->valuestring != NULL)) {
        // printf("City: %s\n", city_item->valuestring);
        return city_item->valuestring;
    }
    return "!_!_!"; // or handle error
}

bool get_element_bool(json *j, const char *key) {
    cJSON *item = cJSON_GetObjectItemCaseSensitive(j->json, key);
    if (cJSON_IsBool(item)) {
        return cJSON_IsTrue(item);
    }
    return false; // or handle error
}

int get_element_int(json *j, const char *key) {
    cJSON *item = cJSON_GetObjectItemCaseSensitive(j->json, key);
    if (cJSON_IsNumber(item)) {
        return item->valueint;
    }
    return 0; // or handle error
}

float get_element_float(json *j, const char *key) {
    cJSON *item = cJSON_GetObjectItemCaseSensitive(j->json, key);
    if (cJSON_IsNumber(item)) {
        return item->valuedouble;
    }
    return 0.0f; // or handle error
}

int close_json(json *j) {
    cJSON_Delete(j->json);
    free(j);
    return 0;
}

char * read_data(const char *json_data_string) {
    //  = "{\"name\": \"Alice\", \"age\": 25, \"city\": \"New York\"}";

    // Parse the JSON string
    cJSON *root = cJSON_Parse(json_data_string);
    char * value = (char *)malloc(256);

    if (root == NULL) {
        const char *error_ptr = cJSON_GetErrorPtr();
        if (error_ptr != NULL) {
            fprintf(stderr, "Error parsing JSON: %s\n", error_ptr);
        }
        return "!_!_!";
    }

    // Access elements
    cJSON *name_item = cJSON_GetObjectItemCaseSensitive(root, "name");
    if (cJSON_IsString(name_item) && (name_item->valuestring != NULL)) {
        printf("Name: %s\n", name_item->valuestring);
    }

    cJSON *age_item = cJSON_GetObjectItemCaseSensitive(root, "age");
    if (cJSON_IsNumber(age_item)) {
        printf("Age: %d\n", age_item->valueint);
    }

    cJSON *city_item = cJSON_GetObjectItemCaseSensitive(root, "city");
    if (cJSON_IsString(city_item) && (city_item->valuestring != NULL)) {
        printf("City: %s\n", city_item->valuestring);
    }

    // Clean up
    cJSON_Delete(root);

    return "!_!_!";
}