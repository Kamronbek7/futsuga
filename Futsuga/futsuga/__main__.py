'''if __name__ == '__main__':
    from os.path import dirname
    from sys import argv
    try: dr = argv[1]
    except IndexError: dr = dirname(__file__)

    from __init__ import Translate
    res = Translate(dr)
    a = res.to_python()
    print(a, "\n"+'='*30+'\n')
    exec(a)'''

from sys import argv, path, executable
import os

path.append('/'.join(os.path.dirname(__file__.replace('\\', '/')).split('/')[:-1]))#r'D:\Files\1_Projects\Futsuga\Futsuga')
path.append(os.path.dirname(__file__))

from langs import read_data
from datas import *

# Main script

ln = 25
cn = '^30'

def help(arg=None):
    if arg == None: print(f'''{'RUN':{cn}}
{'<file>':{ln}}Run <file>
{"-b":{ln}}Run in background
{'-s <log_file_name>':{ln}}Write log any file (optional: <project_name>.log)

{'TRANSLATE':{cn}}
{'--sh':{ln}}translate to .sh  (shell)\tfile. Recommended for little bots
{'--py':{ln}}translate to .py  (Python)\tfile
{'--rs':{ln}}translate to .rs  (Rust)\tfile
{'--cpp':{ln}}translate to .cpp (C++)\tfile

{'ABOUT':{cn}}
{'-v':{ln}}version
{'--py-version':{ln}}python's version

{'SETTINGS':{cn}}
{'--langs':{ln}}Show\tall\tlanguages
{'--set-lang':{ln}}Set\tdefault\tlanguage
{"--lang":{ln}}Show\tnow\tlanguage

CHANGE LOCALHOSTS ADDRESSES
{'--set-editor':{ln}}For editor.\t\t\t\tDefault: http://0.0.0.0:1
{'--set-packs':{ln}}For package and project manager.\tDefault: http://0.0.0.0:7
{'--set-minibot':{ln}}For helper bot.\t\t\tDefault: http://0.0.0.0:3
{'--set-'}

'''.rstrip())

if __name__ == '__main__':
    # from subprocess import getoutput
    try:
        func = argv[1]

        if 'run' == func:
            try: direc = argv[2]
            except IndexError:
                from os.path import dirname
                direc = dirname(__file__)
            from translator import translator
            exec(translator(direc))

        elif func == '-v': print(datas.version)
        elif func == '--py-version': print(datas.py_version)
        elif (func == '-h') or (func == '--help')or (func == '--h')or (func == '/?')or (func == '?'): help()

        elif func == '--langs': print(datas.langs)
        elif func == '--now-lang': print(datas.default_lang)
        
        elif func == '--exe-file': print(executable)

        elif func.split('.')[-1] == 'fga':
            try: open(func)
            except FileNotFoundError: print(read_data(
                text_id='filenotfounderror', lang='uzb', kwargs={'$file': func}
            ))
        else: help()

    except IndexError: help()