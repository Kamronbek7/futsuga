import ast
from functions import *

def cut_parts(line: str) -> dict:
    # Split on first ':' not inside quotes
    inside_single = False
    inside_double = False
    for i, c in enumerate(line):
        if c == "'" and not inside_double:
            inside_single = not inside_single
        elif c == '"' and not inside_single:
            inside_double = not inside_double
        elif c == ':' and not inside_single and not inside_double:
            key = line[:i].strip()
            value = line[i+1:].strip()
            return {key: value}
    return {}

def init_parser(text: str) -> dict:
    def parse_block(lines, indent=0):
        result = {
            'INLINE': True,
            'LOGS': ['ADMINS'],
            'DATABASE_FILE': None
        }
        key = None
        values = []
        while lines:
            line = lines[0]
            if not line.strip() or line.strip().startswith('#'):
                lines.pop(0)
                continue
            curr_indent = len(line) - len(line.lstrip())
            if curr_indent < indent:
                break
            if ':' in line:
                if key is not None:
                    # Save previous key
                    if values:
                        # Try to convert to int/bool if possible
                        result[key] = [ast.literal_eval(v) if v not in ('True', 'False') else v == 'True' for v in values]
                        values = []
                    key = None
                k, v = line.strip().split(':', 1)
                k = k.strip()
                v = v.strip()
                if v:
                    # Inline value
                    try:
                        val = ast.literal_eval(v)
                    except Exception:
                        if v in ('True', 'False'):
                            val = v == 'True'
                        else:
                            val = v
                    result[k] = val
                    lines.pop(0)
                else:
                    # Block value
                    key = k
                    result[key] = []
                    lines.pop(0)
                    # Parse indented block
                    block = []
                    while lines:
                        next_line = lines[0]
                        if not next_line.strip() or next_line.strip().startswith('#'):
                            lines.pop(0)
                            continue
                        next_indent = len(next_line) - len(next_line.lstrip())
                        if next_indent <= curr_indent:
                            break
                        block.append(lines.pop(0).strip())
                    # Recursively parse block
                    if block and any(':' in b for b in block):
                        result[key] = parse_block(block, indent=curr_indent+4)
                    else:
                        # List of values
                        vals = []
                        for b in block:
                            try:
                                val = ast.literal_eval(b)
                            except Exception:
                                if b in ('True', 'False'):
                                    val = b == 'True'
                                else:
                                    val = b
                            vals.append(val)
                        result[key] = vals
            else:
                if key is not None:
                    values.append(line.strip())
                lines.pop(0)
        if key is not None and values:
            result[key] = [ast.literal_eval(v) if v not in ('True', 'False') else v == 'True' for v in values]
        return result

    lines = text.splitlines()
    # Remove comments and empty lines
    lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
    # Remove 'init:' if present
    if lines and lines[0].strip() == 'init:':
        lines = lines[1:]
    return parse_block(lines)

def imports(text: str) -> list:
    data = []
    for line in text.strip().split('\n'):
        if tab_counter(line) == 1:
            if line[-1] == '.' and (not ' ' in line):
                data.append({line[:-1].strip(): '.'})
            elif (' ' in line.strip()) and (line.strip()[-1] != '.'):
                lib, func = line.strip().split(' ')
                data.append({lib: func})
            else:
                data.append({line.strip(): '*'})
        elif line == 'imports:': pass
        else: pass
    return data

def parse_inline_buttons(code: str) -> dict:
    lines = [line.strip() for line in code.splitlines() if line.strip()]
    data = {}
    current_block = None
    current_name = None

    def parse_button_part(part: str):
        # Masalan: URL: "https://t.me/InviProgUz" -> "Salom"
        if ':' in part:
            name, rest = part.split(':', 1)
            name = name.strip()
            rest = rest.strip()
        else:
            name, rest = None, part.strip()

        if '->' in rest:
            value, text = rest.split('->', 1)
            value = value.strip().strip('"\'')
            text = text.strip().strip('"\'')
        else:
            value, text = rest.strip().strip('"\'') if rest else None, None

        return {
            'name': name,
            'value': value,
            'text': text
        }

    for line in lines:
        if line.endswith(':') and not '->' in line:
            # InlineButtons:, menu_btns:, channels:
            key = line[:-1].strip()
            if current_block is None:
                current_block = key
                data[current_block] = {}
            else:
                current_name = key
                data[current_block][current_name] = []
        else:
            # bu yer button qismi
            if '||' in line:
                group = []
                for part in line.split('||'):
                    group.append(parse_button_part(part))
                data[current_block][current_name].append(group)
            else:
                data[current_block][current_name].append(parse_button_part(line))

    return data

def parse_inline_buttons(text):
    def buttons(code):
        btns = {}
        for button in code.split(' || '):
            # print(button)
            name, value = button.split(': ')
            _, text = button.split(' -> ')
            task = ''
            match name:
                case 'URL':
                    task = 'url'
                case 'Copy':
                    task = 'CopyButton'
                case 'Share':
                    task = 'ShareButtons'
                case _:
                    task = 'callback_data'
            btns.update({"name": name, "value": value, "text": text, "task": task})
        return btns
    data = []

    for line in text.strip().split('\n'):
        lines = line.strip()
        if   (tab_counter(line) == 1) and (lines[-1] == ':'):
            data.append({lines[:-1]: {}})

        elif (tab_counter(line) == 2) and (lines[-1] != ':'):
            print(data)
            data.append(buttons(lines))

        elif (tab_counter(line) == 0) and (lines[-1] != ':'): break

        elif lines == 'InlineButtons:': pass

    return data

def keyboard_buttons(code: str) -> dict:
    lines = [line.rstrip() for line in code.splitlines() if line.strip()]
    result = {}
    current_block = None

    for line in lines:
        line = line.strip()
        if line.startswith("KeyboardButtons:"):
            continue

        # yangi bo‘lim (menu, my_account)
        if not line.startswith((" ", "\t")) and line.endswith(":"):
            current_block = line[:-1]
            result[current_block] = []
            continue

        if current_block is None:
            continue

        # tugmalar qatori
        if ":" in line:
            # Masalan: buyurtma: "Buyurtma" || products: "Mahsulotlar"
            row_buttons = []
            for part in line.split("||"):
                part = part.strip()
                if ":" in part:
                    name, text = part.split(":", 1)
                    name = name.strip()
                    text = text.strip().strip('"').strip("'")
                    row_buttons.append({"name": name, "text": text})
            result[current_block].append(row_buttons)

    return result

def parse_commands(text):
    commands = {}
    current_command = None
    
    lines = text.strip().split('\n')
    for line in lines:
        line = line.strip()
        
        if line.startswith('/'):
            # Yangi komanda topildi
            if ':' in line:
                command_name, content = line.split(':', 1)
                command_name = command_name[1:].strip()  # / ni olib tashlash
                content = content.strip()
                
                if content and not content.startswith('\t'):
                    # Oddiy komanda: /command: "text"
                    commands[command_name] = [{
                        'function': 'reply',
                        'text': content.strip('"\'')
                    }]
                    current_command = None
                else:
                    # Ko'p qatorli komanda: /command:
                    commands[command_name] = []
                    current_command = command_name
            else:
                # Faqat komanda nomi
                command_name = line[1:].strip()
                commands[command_name] = []
                current_command = command_name
        
        elif current_command and line:
            # Komanda ichidagi qatorlar
            if ':' in line:
                function_name, content = line.split(':', 1)
                function_name = function_name.strip()
                content = content.strip().strip('"\'')
                
                commands[current_command].append({
                    'function': function_name,
                    'text': content
                })
    # print(commands)
    return commands

def is_python(code: str) -> bool:
    pass

def variables_detector(code: str, line_number=1):
    if (
             char_in_text('=', code
        ) or char_in_text('const ', code
        ) or char_in_text('new ', code)
    ):
        place = 'stack'
        tp = None
        value = None
        name = ''
        tr = True

        if not char_in_text('const ', code) and not char_in_text('new ', code) and not char_in_text('heap ', code):
            name, value = code.split('=')
            value = (eval(value) if not '"' in value or not "'" in value else eval)
            tp = type(value)
        else:
            if char_in_text('const ', code): tr    = False
            if char_in_text('new '  , code): place = 'heap'

        return {
            "what": "variable",
            "place": place.strip(),
            "name": name.strip(),
            "type": tp.strip(),
            "value": value,
            "transfer": tr,
            "meta": {
                "str_line": code,
                "line_number": line_number
            }
        }