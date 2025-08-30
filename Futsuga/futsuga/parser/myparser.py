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

def tab_counter(text, tb='\t'):
    n = 0
    for i in text:
        if i == tb:
            n += 1
        else: break
    return n

def char_in_text(pattern: str, text: str) -> bool:
    inside_single = False
    inside_double = False
    i = 0
    while i < len(text):
        ch = text[i]

        if ch == "'" and not inside_double:
            inside_single = not inside_single
        elif ch == '"' and not inside_single:
            inside_double = not inside_double

        # agar hech qanday qavs ichida emas bo‘lsa, patternni qidiramiz
        if not inside_single and not inside_double:
            if text[i:i+len(pattern)] == pattern:
                return True
        i += 1
    return False

def python_syntax(code):
    pass

def how_code(line: str, tp: str='py'):    # kodni {} larga ega sintaksis bilan tahlil qilish
    if   '@cpp'    == line:     # indetlarni {} qilib belgilash
        return    'cpp'
    elif '@python' == line:     # sintaksisni python'dagidek qilish, funksiyalarni unga sozlash
        return 'python'
    
    elif ((tp == 'cpp') and (line.strip()[-1] == '{')
                            ) or (
                                (tp == 'py') and (line.strip()[-1] == ':')
                            ):     # indent
        c = f'begin.'
        nline = line[:-1].strip()

        if (nline in body):     # body indentlar
            return c+nline
        
        elif (char_in_text('is_', line)) or (char_in_text(' not ', line)): # if, else kabilar
            return c[:-1]+'.if.'+nline
        
        else: return c+nline
        
    elif (tp == 'cpp') and ((line.strip() == '}') or (line.strip()[-1] == '}')): # {} by deindent
        c = 'end'
        if line.strip().replace('}', '') == '': # } dan boshqa narsa bor-yo'qligini tekshirish
            return c+'.'+str(tab_counter(line[::-1], '}'))
        
    elif ('/' == line.strip()[0]):
        return 'command'
    
    elif (tp == 'py') and (char_in_text(': ', line)) and (line[0] != ':') and (line[-1] != ':'): # a: b ko'rinishidagi datani o'qish
        name, _ = line.strip().split(':', 1)

        if char_in_text(' -> ', line):          # tugmalarni -> bilan ajratib olish
                if char_in_text(': ', line):    # tugma turini aniqlash
                    return f'assign_buttons.inline.{line.split(' ', 2)[0].strip(':')}'
                
                return 'assign_buttons'
        
        elif (line.strip().split(': ')[0] in functions): return 'call_function'

        elif (not char_in_text(name, functions)) or (char_in_text('is_', line)): # funksiya chaqirilmayotganini tekshirish
            if (
                not char_in_text(name, functions)
            ) and (
                char_in_text('is_', line)
            ) and (
                not char_in_text(' || ', line)
            ) and (
                not char_in_text(' -> ', line)
            ) and (
                not char_in_text(name, dir(file_handlers))
            ): return 'assign'                  # o'zgaruvchi yoki belgilash kiritish

            elif (char_in_text(' || ', line)) or (char_in_text(' -> ', line)):   # tugmalarni aniqlash
                if (char_in_text(' -> ', line)):                                 # keyboard
                    return f'assign_buttons.keyboard.{line.split(': ', 2)[0]}'
                
                elif (char_in_text(' -> ', line)): return f"assign_buttons.inline.{line.split(': ', 2)[0]}" # inline

            elif (char_in_text('is_', line)) or (char_in_text('not', line)):     # if, else tekshiruvi
                return 'if.' + line.split(': ')[0].strip()
        
        if (char_in_text(name, dir(file_handlers))) and (char_in_text(name, functions)):
            return 'call_function'
            
        else: return f'call_function'

    else:
        try:
            a = eval(line)
            for i in (str, float, int, tuple, dict, list, set): # qiymat kiritilayotganini tekshirish
                if isinstance(a, i):
                    return 'value'
                
        except SyntaxError:                                     # python'ga aloqasi bor-yo'qligini tekshirish
            if char_in_text(' -> ', line):                      # tugmalarni tahlil qilish

                if not char_in_text(': ', line):
                    return f'assign_buttons.inline.{line.split(' ', 2)[0].strip(':')}'
                
                elif line.find(':') < line.find('->') and (not char_in_text(' -> ', line)):
                    return f'assign_buttons.keyboard.{line.split(':', 2)[0].strip(':')}'
                
                return 'assign_buttons'
            
            elif ('pass' == line.strip()) or (char_in_text('return ', line)): return 'py_key' # py keywordlarini aniqlash
        
            else:
                if (char_in_text('py.', line)): return 'py_func' # py funksiya va kutubxona metodlarini aniqlash
                elif (char_in_text(': ', line)) and (line.strip()[0].isalpha()):
                    if (line.find(': ') > 1): return f'call_function.{line.find(": ")}'
                    return 'assign' # o'zgaruvchi yoki qiymat berish
                
                elif (char_in_text(': ', line)) and (line.strip()[0] in ('"', "'")): return 'reply_to_text'

                return 'unknown'              # noma'lum kod
            
        except NameError:
            if (char_in_text('py.', line)): # py funksiyani aniqlash
                return 'py_call'
    
            return 'call_value'
        
        except Exception as e: return 'Error: ' + str(e) # xatolik

class futs_to_json:
    def __init__(self, code):
        self.code = code
        self.pydict = dict()

    def python(self, code) -> str:
        return code

    def init(self, code):
        data = {}
        for i in code:
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

def futs_to_py(code: str) -> str:
    pass

def futs_analyzer(code):
    # pycode = ''
    # datas = dict()
    n = 0
    lang = 'py'
    fl = open('st.md', 'wb')
    fl.write(b'|Line|Turi|Data|\n|-|-|-|\n')
    for line in remove_comments(r"D:\Files\1_Projects\Futsuga\Examples\sample_bot\main.fga").replace('|', '/./').split('\n'):
        n += 1
        res = ''
        if line.strip() == '': continue
        else: res = how_code(line)
        if res in ('cpp', 'py'): lang = res
        try:
            fl.write(f'|{n}|{how_code(line, lang)}|{line.strip()}|\n'.encode())
        except Exception as e:
            print(e, line)
    fl.close()

if __name__ == '__main__':
    futs_analyzer('a')