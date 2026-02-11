import re
from .constantas import *

def remove_comments(input_path):
    "kodni izohlardan tozalaydi"
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

    if '\n' in input_path:
        content = input_path
    else:
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
    'tab larni sanaydi "    " 1 tab deb olinadi'
    n = 0
    for i in text:
        if i == tb: n += 1
        else: break
    if n == 0:
        for i in text:
            if i == ' ': n += 1
            else: return n//4
    return n

def cut_word_by_char(text: str, char: str = ' ') -> list:
    "biror belgi yoki satr bo'yicha text'ni ajratadi"
    result = []
    current = ''
    inside_single = False
    inside_double = False
    i = 0
    while i < len(text):
        c = text[i]
        if c == "'" and not inside_double:
            inside_single = not inside_single
            current += c
        elif c == '"' and not inside_single:
            inside_double = not inside_double
            current += c
        elif c == char and not inside_single and not inside_double:
            result.append(current)
            current = ''
        else:
            current += c
        i += 1
    result.append(current)
    return result

def char_in_text(pattern: str, text: str) -> bool:
    "bir belgi boshqasining ichida ekanligini aniqlaydi. '' ichidagi matnlar hisobga olinmaydi"
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

def indent_equalizer(code):
    "indentlarni tekislaydi"
    tabs = []
    new_code = ''
    for line in code.splitlines():
        tb = tab_counter(line)
        if tb not in tabs:
            tabs.append(tb)
    min_tabs = min(tabs)
    for line in code.splitlines():
        lines = line.strip()
        tb = tab_counter(line)
        new_line = '\t'*(tb-min_tabs) + (line.strip())
        new_code += f'\n{new_line}'
    return new_code

def charintexttpl(code, chars=[
        'return ', 'break', '=', '==', '!=',
        '<', '>', 'def ', 'class ', 'import',
        'from ', '+', '-', '*', '//', '**',
        '%', 'raise ', 'lambda ', '()', '(', ')',
        '[]', '[', ']', '{}', '{', '}', 'dict',
        'type(', 'print', 'dir', 'for ', ' in ',
        'if', 'else', 'elif', 'pass', 'str', 'int',
        'tuple', 'list', '<', 'input', ':='
        ]):
    "code ichida chars borligini tekshirib chiqadi. Har bir belgi alohida tekshiriladi"
    for char in chars:
        if char_in_text(char, code):
            return True
    return False

def is_python(code):
    "ushbu kod pythonga tegishli ekanligini aniqlash"
    return charintexttpl(code)

def how_code(line: str, block: str=None, header: str=None) -> str:
    "kod haqida ma'lumot beradi"
    lines = line.strip()
    tabs  = tab_counter(line)
    ret   = f'{tabs}.'

    if ((line.strip()[-1] == ':')
            ) or (
                (line.strip()[-1] == ':')
            ):     # indent
        c = ret + 'new.'
        nline = line[:-1].strip()

        if (nline in body):     # body indentlar
            return f'{ret}begin.{line[:-1]}'
        
        # elif (char_in_text('is_', line)) or (char_in_text(' not ', line)): # if, else kabilar
        #     return c[:-1]+'.if.'+nline
        
        else: return c+nline

    elif ('/' == line[0]): # buyruqlarni
        return ret + 'command'
    
    elif ('if' == lines[:2] or 'else' == lines[:4] or 'elif' == lines[:4]): # shartlarni
        return ret + f'if.{lines.split(" ", 2)[0]}'
    
    elif (char_in_text('=', lines)): # o'zgaruvchilar
        return ret + 'assign'
    
    elif (line[0] == '~' or line[0] == '"' or line[0] == "'"): # MessageHandler's
        return ret + 'text'
    
    elif (char_in_text(': ', line)) and (line[0] != ':') and (line[-1] != ':'): # a: b ko'rinishidagi data
        name, _ = line.strip().split(':', 1)

        if char_in_text(' -> ', line):          # tugmalarni -> bilan ajratish
                if char_in_text(': ', line):    # tugma turini
                    return f'{ret}assign_buttons.inline.{line.split(' ', 2)[0].strip(':').strip()}'
                
                return f'{ret}assign_buttons'
        
        elif (line.strip().split(': ')[0] in functions): return f'{ret}call_function' # funksiya chqiruvini

        elif (not char_in_text(name, functions)) or (char_in_text('is_', line)): # funksiya chaqirilmayotgani
            if (
                not char_in_text(name, functions)
            # ) and (
                # not char_in_text('is_', line)
            ) and (
                not char_in_text(' || ', line)
            ) and (
                not char_in_text(' -> ', line)
            ) and (
                not char_in_text(name, dir(file_handlers))
            ):
                if lines.strip(':') in body:
                    return ret + 'def.' + lines.strip(':')
                else:
                    return ret + 'arging'                  # o'zgaruvchi yoki belgilash kiritish

            elif (char_in_text(' || ', line)) or (char_in_text(' -> ', line)):   # tugmalarni aniqlash
                if (char_in_text(' -> ', line)):                                 # keyboard
                    return f'{ret}assign_buttons.keyboard.{line.split(': ', 2)[0]}'
                
                elif (char_in_text(' -> ', line)): return f"{ret}assign_buttons.inline.{line.split(': ', 2)[0]}" # inline

            # elif (char_in_text('is_', line)) or (char_in_text('not', line)):     # if, else tekshiruvi
            #     return f'{ret}if.' + line.split(': ')[0].strip()
        
        if (char_in_text(name, dir(file_handlers))) and (char_in_text(name, functions)):
            return ret + 'call_function'
            
        else: return ret + f'call_function'

    else:
        try:
            a = eval(line)
            for i in (str, float, int, tuple, dict, list, set): # qiymat kiritilayotganini tekshirish
                if isinstance(a, i):
                    return ret + 'value'
                
        except SyntaxError:                                     # python'ga aloqasi bor-yo'qligini tekshirish
            if char_in_text(' -> ', line):                      # tugmalarni tahlil qilish

                if not char_in_text(': ', line):
                    return ret + f'assign_buttons.inline.{line.split(' ', 2)[0].strip(':')}'
                
                elif line.find(':') < line.find('->') and (not char_in_text(' -> ', line)):
                    return ret + f'assign_buttons.keyboard.{line.split(':', 2)[0].strip(':')}'
                
                return ret + 'assign_buttons'
            
            elif ('pass' == line.strip()) or (char_in_text('return ', line)): return ret + 'py_key' # py keywordlarini aniqlash
        
            else:
                if (char_in_text('py.', line)): return ret + 'py_func' # py funksiya va kutubxona metodlarini aniqlash
                elif (char_in_text(': ', line)) and (line.strip()[0].isalpha()):
                    if (line.find(': ') > 1): return ret + f'call_function.{line.find(": ")}'
                    return 'assign' # o'zgaruvchi yoki qiymat berish
                
                elif (char_in_text(': ', line)) and (line.strip()[0] in ('"', "'")): return ret + 'reply_to_text'

                elif (lines.strip('.').split('.')[0].strip('*') in libraries):
                    tp = ''
                    if          lines[-1] == '.': tp = 'class'
                    elif        lines[-1] == '*': tp = 'all'
                    elif ' ' in lines           : tp = 'some'
                    return ret + 'library.' + lines.strip('.').split('.')[0].strip('*') + '.' + tp

                return ret + str(i if is_python(line) else 'unknown')              # noma'lum kod
            
        except NameError:
            if (char_in_text('py.', line)): # py funksiyani aniqlash
                return ret + 'py_call'
    
            return     ret + 'call_value'
        
        except Exception as e: return ret + 'Error: ' + str(e) # xatolik

def body_splitter(code):
    "kodning init, commands kabi qismlarini bo'laklarga ajratadi"
    old = None
    data = {}
    for line in code.split('\n'):
        res = ''
        if line.strip() == '': continue
        else:
            res = how_code(line, old)
            old = res
            indent = int(res.split('.')[0])

            if   (indent == 0) and     (line[-1] == ':'):
                data.update({line[:-1].strip(): ''})

            elif (indent != 0) and not (line[-1] == ':'):
                data[list(data)[-1]] += f'\n{line}'
    return data

def part_splitter(code) -> list:
    "kodni bo'laklarga ajratish"
    parts      = {}
    now_block  = []
    old_indent = 0
    now_code   = []
    partnum    = 0
    for line in code.split('\n'):
        data = how_code(line)
        sdata = data.split('.')
        now_indent = int(sdata[0])
        if   now_indent == old_indent:
            print('now')
            now_code.append(line.strip())
        elif now_indent >  old_indent:
            print('new')
        elif now_indent <  old_indent:
            print('closed')
        elif now_indent == 0:
            print('end block')
            partnum += 1
            parts.update({f'part{partnum}': '\n'.join(now_code)})
            now_code = []
        old_indent = now_indent
    return parts