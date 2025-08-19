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


def remove_comments(input_path):
    code = ''
    def remove_inline_comments(line):
        # Remove # comments not inside quotes
        in_quote = False
        quote_char = ''
        new_line = ''
        i = 0
        while i < len(line):
            c = line[i]
            if c in ('"', "'"):
                if not in_quote:
                    in_quote = True
                    quote_char = c
                elif quote_char == c:
                    in_quote = False
            if c == '#' and not in_quote:
                break
            new_line += c
            i += 1
        return new_line.rstrip()

    def remove_block_comments(text):
        # Remove /* ... */ comments, even multiline, but NOT inside quotes
        pattern = re.compile(r'/\*.*?\*/', re.DOTALL)
        result = ''
        i = 0
        while i < len(text):
            m = pattern.search(text, i)
            if not m:
                result += text[i:]
                break
            before = text[:m.start()]
            # Count quotes before block
            double_quotes = before.count('"') - before.count('\\"')
            single_quotes = before.count("'") - before.count("\\'")
            # Only remove if not inside quotes
            if double_quotes % 2 == 0 and single_quotes % 2 == 0:
                result += text[i:m.start()]
                i = m.end()
            else:
                result += text[i:m.end()]
                i = m.end()
        return result

    with open(input_path, encoding='utf-8') as fin:
        content = fin.read()
        content = remove_block_comments(content)
        lines = content.splitlines()

    # with open(output_path, 'w', encoding='utf-8') as fout:
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('#') or not stripped.strip():
            continue
        line_no_inline = remove_inline_comments(line)
        if line_no_inline.strip():
            code += line_no_inline + '\n' #fout.write(line_no_inline + '\n')
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

'''
1. futs_to_json class'i
2. Ichki parserlar:
    * python kodni aniqlovchi
    * o'zgaruvchilarni parse qiluvchilar
    * asosiy bo'limlar (init, imports, ...)
    * argumentlarni parse qiluvchilar
    * funksiyalarni parse qiluvchilar (argumentlar bilan)
    * tugmalarni parse qiluvchilar
    * buyruqlarni parse qiluvchilar
    * message_handlerlarni parse qiluvchilar
    * is_* kabilarni parse qiluvchilar
3. asosiy to'liq parse qiluvchi metod
4. json'ga o'girish
5. pythonga o'girish
6. flaglar asosida ishga tushirish
'''