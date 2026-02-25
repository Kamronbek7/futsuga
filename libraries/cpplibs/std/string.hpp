#include <cstring>
#include <sstream>
#include <iostream>
#include "mathematics.hpp"

const char * ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
const char * ascii_lowercase = "abcdefghijklmnopqrstuvwxyz";
const char * ascii_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const char * digits = "0123456789";
const char * hexdigits = "0123456789abcdefABCDEF";
const char * octdigits = "01234567";
const char * printable = "'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c";
const char * punctuation = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~";
const char * whitespace = " \t\n\r\x0b\x0c";

std::string center(const std::string text, const unsigned int width, const char chr=' ') {
    std::stringstream text2;

    int half  = (width-strlen(text.c_str())) / 2;
    int half2 = half;

    if (half < 1) return text;

    if (is_odd(half)) {
        half++;
    }
    
    for (half; half > 0; half--) {
        text2 << chr;
    }

    text2 << text;
    
    for (half2; half2 > 0; half2--) {
        text2 << chr;
    }
    
    return text2.str();
}

std::string left(const std::string text, const unsigned int width, const char chr=' ') {
    std::stringstream text2;

    int half  = width-strlen(text.c_str());

    if (half < 1) return text;

    for (half; half > 0; half--) {
        text2 << chr;
    }
    text2 << text;

    return text2.str();
}

std::string right(const std::string text, const unsigned int width, const char chr=' ') {
    std::stringstream text2;

    int half  = width-strlen(text.c_str());

    if (half < 1) return text;
    text2 << text;

    for (half; half > 0; half--) {
        text2 << chr;
    }

    return text2.str();
}