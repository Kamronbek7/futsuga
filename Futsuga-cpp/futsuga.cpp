#include <iostream>
#include <string>
#include <vector>
#include <format>

std::string ljust(std::string str, size_t width, char pad = ' ') {
    if (width > str.length()) {
        str.append(width - str.length(), pad);
    }
    return str;
}

constexpr size_t LENGTH = 25;

class help_objects {
    public:
    std::string version = "v1.0.0a2";
};

void help(std::string arg="") {
    if (arg == "") {
        std::cout << std::format("{:^{}}", "RUN", LENGTH) << std::endl;
    }
}

std::string find_args(const std::string arg, const std::vector<std::string> args) {
    return "";
}

int main(int argc, char * argv[]) {
    help();
    return 0;
}