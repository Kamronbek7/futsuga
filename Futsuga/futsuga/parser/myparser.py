from constantas import *
# from ast import *
import re
# print(dir())

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

body = [
    'init',
    'imports',
    'InlineButtons',
    'commands',
    'text',
    'admin_panel',
    'files',
    'keyboard_buttons_handler',
    'inline_buttons_handler',
    'chat_handlers'
]

class params:
    admins   = 'ADMINS'
    token    = 'TOKEN'
    webhook  = 'WEBHOOK'
    database = 'DATABASE'
    inline   = 'INLINE'

class buttons:
    inline         = 'InlineButton'
    keyboard       = 'KeyboardButton'
    command_button = 'CommandButtons'

class file_handlers:
    file       = 'FILE'
    photo      = 'PHOTO'
    video      = 'video'.upper()
    video_note = 'video_note'.upper()
    audio      = 'AUDIO'

class_to_list = lambda name: list(eval(f'{name.__name__}.{i}') for i in dir(name) if '__' not in i)

def tab_counter(text, tb='\t'):
    n = 0
    for i in text:
        if i == tb:
            n += 1
        else: break
    return n

def python_syntax(code):
    pass

def how_code_cpp(line: str): # kodni {} larga ega sintaksis bilan tahlil qilish
    if (line.strip()[-1] == '{'):     # indent
        c = f'begin.'#.{tab_counter(line)},'
        nline = line[:-1].strip()
        if (nline in body): # body indentlar
            return c+nline
        elif ('is_' in line) or ('not' in line):
            return c[:-1]+'.if,'+nline
        else:
            return c+nline
        
    elif (line.strip() == '}') or (line.strip()[-1] == '}'): # {} by deindent
        c = 'end'
        if line.strip().replace('}', '') == '':
            return c+'.'+str(tab_counter(line[::-1], '}'))
    
    elif (':' in line) and (line[0] != ':') and (line[-1] != ':'): # a: b ko'rinishidagi datani o'qish
        name, _ = line.strip().split(':', 1)
        # if isinstance(value, str): value = f'"{value}"'
        if not name in functions:
            return 'assign'
        elif ' -> ' in line:
            return 'assign_buttons'
        else: return f'do.{name}'

    else:
        try:
            a = eval(line)
            for i in (str, float, int, tuple, dict, list, set):
                if isinstance(a, i):
                    return 'value'
        except SyntaxError:
            if '->' in line:
                return 'assign_buttons'
            
            elif ('@cpp' == line): return '{}'    
        
            return 'unknown'
        except NameError:
            if ('py.' in line) or ('pass' in line):
                return 'py_call'
    
            return 'call_value'
        except Exception as e: return 'Error: ' + str(e)

def how_code(line): # kodni tahlil qilish
    tabs = tab_counter(line)
    # tich = ':', '{'
    c = ''
    if   '@cpp'    == line:     # indetlarni {} qilib belgilash
        return    'cpp'
    elif '@python' == line:     # sintaksisni python'dagidek qilish, funksiyalarni unga sozlash
        return 'syntax.python'
    
    elif   (line[-1] == ':'):                         # indent boshlanganligini aniqlash
        c = 'begin,'
        if (line[:-1] in body) and (line[0] != '\t'): # tana qismiga tegishli indentlar
            return c+'body,'+line[:-1]
    
    elif line[0] == '\t':                             # mavjud indentni aniqlash
        c = f'indent.{tabs},'
        if (':' in line) and (line[0] != ':') and (line[-1] != ':'
                                                   ): # a: b ko'rinishidagi datani o'qish
            # name, value = line.strip().split(':', 1)
            # if isinstance(value, str): value = f'"{value}"'
            return c+'assign'
        
    elif line[0] != '\t':                             # indent 0 bo'lgan holatni aniqlash
        pass

    # elif : # python yoki yo'q
    # pass

    else: return 'Unknown: ' + line
    return c

class futs_to_json:
    def __init__(self, code):
        self.code = code
        self.pydict = dict()

    def python(self):
        pass

    def body(self):
        pass

    def function(self):
        pass

    def inline_buttons(self):
        pass

    def values(self):
        pass

    def commands(self):
        pass

    def if_is(self):
        pass

    def keyboard_buttons(self):
        pass

    def total(self):
        pass

def futs_to_py(code):
    pycode = ''
    datas = dict()
    n = 0
    fl = open('st.md', 'wb')
    fl.write(b'|Line|Turi|Data|\n|-|-|-|\n')
    for line in remove_comments(r"D:\Files\1_Projects\Futsuga\Examples\sample_bot\main_cpp.fga").replace('|', '/./').split('\n'):
        # print(dump(parse(line)))
        n += 1
        if line.strip() == '': continue
        try:
            fl.write(f'|{n}|{how_code_cpp(line)}|{line.strip()}|\n'.encode())
            # print(how_code(line), n, '\t\t', line)
        except IndexError as e:
            print(e, line)
            # fl.write(f'| {n} | Error: {e} | {line}|\n'.encode())
        except Exception as e:
            print(e, line)
            # fl.write(f'| {n} | Error: {e} | {line}|\n'.encode())
        # if line.strip() != '' and line.strip()[-1] == ':':
        #     print(f'"{line.strip()[:-1]}":')
    fl.close()

if __name__ == '__main__':
    futs_to_py('a')