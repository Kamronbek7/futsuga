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

def help(arg=None):
    if arg == None: print(f'''{'RUN':^30}
{'<file>':<25}Run <file>
{"-b":<25}Run in background
{'-s <log_file_name>':<25}Write log any file (optional: <project_name>.log)

{'ABOUT':^30}
{'-v':<25}version
{'--py-version':<25}python's version

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
        elif (func == '-h') or (func == '--help'): help()
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