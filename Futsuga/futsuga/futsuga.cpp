#include <iostream>
#include <sstream>
#include <fstream>

int main(int argc, char * args[]) {
    std::ostringstream txt;
    txt << "\t\t\t\tRUN\n" <<
"<file>\t\tRun <file>\n" <<
"-b\t\tRun in background\n" <<
"-s <log_file_name>\t\tWrite log any file (optional: <project_name>.log)\n\n" <<

"\t\t\t\tTRANSLATE\n" <<
"--sh\t\ttranslate to .sh  (shell)\tfile. Recommended for little bots\n" <<
"--py\t\ttranslate to .py  (Python)\tfile\n" <<
"--rs\t\ttranslate to .rs  (Rust)\tfile\n" <<
"--cpp\t\ttranslate to .cpp (C++)\tfile\n\n" <<

"\t\t\t\tABOUT\n" <<
"-v\t\tversion\n" <<
"--py-version\t\tpython's version\n\n" <<

"\t\t\t\tSETTINGS\n" <<
"--langs\t\tShow\tall\tlanguages\n" <<
"--set-lang\tSet\tdefault\tlanguage\n" <<
"--lang\t\tShow\tnow\tlanguage\n\n" <<

"\t\t\t\tCHANGE LOCALHOSTS ADDRESSES\n" <<
"--set-editor\t\tFor editor.\t\t\t\tDefault: http://0.0.0.0:1\n" <<
"--set-packs\t\tFor package and project manager.\tDefault: http://0.0.0.0:7\n" <<
"--set-minibot\t\tFor helper bot.\t\t\t\tDefault: http://0.0.0.0:3";
    try {
        std::string func = args[1];
        if      (func == "-h" or func == "?" or func == "--help") std::cout << "This is Futsuga\n";
        else if (func.find(".futs")!=std::string::npos) {
            std::ifstream file;
            file.open(func, std::ios::);
        }
        else {
            std::cout << "Incorrect command. You write \'futsuga ?\' for help.";
        }
    } catch(...) {
        std::cout << txt.str();
    }
    
}