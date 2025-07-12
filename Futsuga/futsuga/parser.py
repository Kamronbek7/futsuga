import re

def main_env(direc):
    if direc[-1] not in ('/', '\\'): direc += '/'
    env_file = direc + '.env'
    try:
        fl = open(env_file)
        txt = fl.read().strip()
        fl.close()

        txt2 = ''

        for i in txt.split('\n'):
            if i[0] != '#': txt2 += i+'\n'
        return txt2
    except FileNotFoundError:
        return f'Fayl topilmadi: "{env_file}"'

def requirements(direc):
    if direc[-1] not in ('/', '\\'): direc += '/'
    req_file = direc + 'requirements.txt'
    return "print('hello')"

def py_parser(code):
    pass

def hash_comment(line):
    line2 = ''
    for i in line:
        if i == '#':
            return line2
        else: line2 += i

def translator(file):
    code = ''
    # from os import path
    # dr = path.dirname(file)
    a = (
        main_env(file),
        requirements(file)
    )
    code += '\n'.join(a).strip()
    return code

# Example code generation stub

def generate_python_code(parsed: dict) -> str:
    lines = ["from telegram import *", f'TOKEN = "{parsed["TOKEN"]}"', ""]
    for cmd, actions in parsed['Commands'].items():
        cmd_name = cmd.lstrip('/')
        lines.append(f"async def {cmd_name}(update, context):")
        for action in actions:
            lines.append(f"    # {action}")
        lines.append("")
    return '\n'.join(lines)

def remove_comments(code: str) -> str:
    code = code.decode()
    def remove_outside_quotes(text, pattern):
        result = []
        in_single = in_double = in_triple_single = in_triple_double = False
        i = 0
        while i < len(text):
            ch = text[i]
            next3 = text[i:i+3]
            # Detect triple quotes
            if next3 == "'''" and not in_double and not in_triple_double:
                in_triple_single = not in_triple_single
                i += 3
                continue
            elif next3 == '\"\"\"' and not in_single and not in_triple_single:
                in_triple_double = not in_triple_double
                i += 3
                continue
            elif ch == "'" and not in_double and not in_triple_double and not in_triple_single:
                in_single = not in_single
                i += 1
                continue
            elif ch == '"' and not in_single and not in_triple_double and not in_triple_single:
                in_double = not in_double
                i += 1
                continue

            if not in_single and not in_double and not in_triple_single and not in_triple_double:
                if pattern == '#' and ch == '#':
                    # Ignore comment till end of line
                    while i < len(text) and text[i] != '\n':
                        i += 1
                    continue
            result.append(ch)
            i += 1
        return ''.join(result)

    # Step 1: Remove multiline comments outside quotes
    code = re.sub(r"(?s)(?<!['\"])\s*'''(.*?)'''", '', code)
    code = re.sub(r'(?s)(?<!["\'])\s*"""(.*?)"""', '', code)

    # Step 2: Remove # comments outside strings
    code = remove_outside_quotes(code, '#')

    return code

class params:
    admins = 'ADMINS'
    token = 'TOKEN'
    webhook = 'WEBHOOK'
    database = 'DATABASE'
    inline = 'INLINE'

class buttons:
    inline = 'InlineButton'
    keyboard = 'KeyboardButton'
    command_button = 'CommandButtons'

class file_handlers:
    file = 'FILE'
    photo = 'PHOTO'
    video = 'video'.upper()
    video_note = 'video_note'.upper()
    audio = 'AUDIO'

class_to_list = lambda name: list(eval(f'{name.__name__}.{i}') for i in dir(name) if '__' not in i)

# print(class_to_list(params))
# import sys; sys.exit()

def file_parser(file):
    code = file.read()
    try: code = code.decode()
    except: pass
    codepc = code.strip().split('\n')
    ln = 0
    parse = ''
    while ln < len(codepc):
        print(ln)
        line = codepc[ln]
        linep = line.strip()
        if linep == '': ln += 1
        elif linep[0] == '#': ln += 1
        # elif linep[-1] == ':':
        #     pass
        elif linep.replace(' ', '') == 'config:':
            while not codepc[ln][0] in (' ', '\t', '       '):
                ln +=1 
                cd = codepc[ln].strip()

        elif '=' in line and line.split('=')[0].strip().isupper():
            if line.split('=') in class_to_list(params):
                pr, value = line.split('=')
                parse += f'{pr.strip()} = "{value.strip()}"\n'
                print(parse)
            ln += 1; continue
        elif ':' in line and '#' not in line:
            parse += f'{line.split(':')[0]} = '
            ln += 1
            print(f'"{codepc[ln][0]}"')
            try:
                while codepc[ln][0] in (' ', '\t', '       ') and (len(codepc)>ln):
                    parse += codepc[ln] + ','
                    ln += 1
                else: parse += '\n'; ln += 1
            except IndexError as e:
                print(e, ln)
        else: ln += 1
    return parse

# Main class
class Translate:
    def __init__(self, file):
        self.file = file
        self.code = ''
        if file[-1] not in ('/', '\\'): file += '/'
        try: open(file+'src/main.fga')
        except FileNotFoundError: print("Fayl mavjud emas")
    
    def to_python(self):
        return translator(self.file)

if __name__ == '__main__':
    # from sys import argv
    # print(translator(argv[1]))
    # file_parser(r"D:\Files\1_Projects\Futsuga\_excample\src\excample.fga")
    # print(
    #     generate_python_code(
    #         parse_futsuga_to_dict(
    #             remove_comments(
    #                 open(r"D:\Files\1_Projects\Futsuga\_excample\src\excample.fga").read()
    #             )
    #         )
    #     )
    # )
    print(
        file_parser(open(r"D:\Files\1_Projects\Futsuga\_excample\src\excample.fga", 'rb'))
    )