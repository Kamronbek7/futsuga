import re

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
        if i == tb: n += 1
        else: break
    if n == 0:
        for i in text:
            if i == ' ': n += 1
            else: return n//4
    return n

def cut_word_by_char(text: str, char: str = ' ') -> list:
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