import json
import re
import colorama as color

color.init(True)

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

'''def parse_fga(filename):
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()

    result = {}
    stack = [result]
    indents = [0]
    key_stack = [None]

    def get_indent(line):
        # Count tabs for indentation
        return len(line) - len(line.lstrip('\t'))

    for raw in lines:
        line = raw.rstrip('\n')
        if not line.strip() or line.strip().startswith('#'):
            continue
        indent = get_indent(line)
        content = line.lstrip('\t')

        # Adjust stack for current indent
        while indent < indents[-1]:
            stack.pop()
            indents.pop()
            key_stack.pop()

        # Section or key detection
        if content.endswith(':'):
            key = content[:-1].strip()
            stack[-1][key] = {}
            stack.append(stack[-1][key])
            indents.append(indent + 1)
            key_stack.append(key)
        elif ':' in content:
            key, val = content.split(':', 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            # Special case for warnings=True/False
            if key.lower() == "warnings" and val.lower() in ("true", "false"):
                stack[-1][key] = val.lower() == "true"
            elif not val:
                stack[-1][key] = []
                stack.append(stack[-1][key])
                indents.append(indent + 1)
                key_stack.append(key)
            else:
                stack[-1][key] = val
        elif '->' in content:
            text, rest = content.split('->', 1)
            text = text.strip().strip('"').strip("'")
            if ':' in rest:
                subkey, subval = rest.split(':', 1)
                subkey = subkey.strip()
                subval = subval.strip().strip('"').strip("'")
                # Special case for warnings=True/False in inline
                if subkey.lower() == "warnings" and subval.lower() in ("true", "false"):
                    subval = subval.lower() == "true"
                if isinstance(stack[-1], list):
                    stack[-1].append({ "text": text, subkey: subval })
                else:
                    stack[-1][text] = {subkey: subval}
            else:
                if isinstance(stack[-1], list):
                    stack[-1].append({ "text": text, "value": rest.strip() })
                else:
                    stack[-1][text] = rest.strip()
        elif content.startswith('"') or content.startswith("'"):
            val = content.strip('"').strip("'")
            if isinstance(stack[-1], list):
                stack[-1].append(val)
            else:
                stack[-1][val] = None
        else:
            val = content.strip()
            if isinstance(stack[-1], list):
                stack[-1].append(val)
            else:
                stack[-1][val] = None

    def convert_lists(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                obj[k] = convert_lists(v)
        elif isinstance(obj, list):
            if all(isinstance(x, str) and x.isdigit() for x in obj):
                return [str(x) for x in obj]
            else:
                return [convert_lists(x) for x in obj]
        return obj

    return convert_lists(result)'''

class main_parser:
    def __init__(self, code):
        self.code = code
        self.code_list = code.split('\n')
        self.tpl = ('    ', '\t', '  ')
        self.init = {
            "TOKEN": ".env",
            "ADMINS": [],
            "INLINE": True,
            "ADMIN_WARNINGS": True,
            "LOGS": {
                "file": "file.log",
                "telegram": "ADMINS"
            },
            "DATABASE": "dbs/users",
            "WEBHOOK": False,
            "TASK": False
        }
    def get_init(self):
        code: dict = {}
        for i in self.code_list:
            i = i[1:]
            if i.strip() == '':
                st = i.strip().split(':').strip()
                print(f'"{st[0]}":"{st[1]}"')
                # return code
            elif i[0] in self.tpl and i[1] in self.tpl:
                pass  # TODO: Implement logic here
        return code
                

def parser2(filename):
    code = remove_comments(filename)
    tpl = ('    ', '\t', '  ')
    data = {
        "init": {
            "TOKEN": ".env",
            "ADMINS": [],
            "INLINE": True,
            "ADMIN_WARNINGS": True,
            "LOGS": {
                "file": "file.log",
                "telegram": "ADMINS"
            },
            "DATABASE": "dbs/users",
            "WEBHOOK": False,
            "TASK": False
        },
        "imports": [],
        "InlineButtons": [],
        "KeyboardButtons": [],
        "commands": {},
        "text": {},
        "admin_panel": {
            "commands": ["/admin", "/subscribers"],
        },
        "files": {},
        "keyboard_handler": {},
        "inline_handler": {},
        "chat_handlers": {}
    }

    nums = dict()
    nums_tpl = tuple(nums)
    
    all = tuple(data)
    
    for line in code.split('\n'):
        # print(line, end=' ')
        line_s = line.strip()
        line_r = line.rstrip()
        # print(1 in tuple(nums.values()))
        if   line_s == '': pass
        elif ':' == line[-1] and ' ' not in line:
            print(line.replace(r'(*.): ', '": "'))
        elif (1 in tuple(nums.values())) and (line_r[0] in tpl): # tab bor va avvalgi qiymat 1
            # print('1 bor')
            if (line[0] in tpl): # tab bor
                pass
            elif (line[0] not in tpl): # tab yo'q
                # for i in nums:
                #     if i == 1: nums[i] = 0
                nums.pop(line[:-1])
                nums[line[0]] = (i for i in nums_tpl if nums[i] == 1)
                print('tab tugadi')
        elif (line_r[:-1] in all) and (1 not in nums_tpl):
            nums[line_r] = 1
            print(f'{color.Fore.GREEN}{nums}')
        elif (line_r[:-1] not in all) and (line[0] not in tpl):
            nums.popitem()
        else:
            print(f'{color.Fore.LIGHTBLUE_EX} {line}{color.Fore.RESET}')
    return data

file = r"D:\Files\1_Projects\Futsuga\Examples\sample_bot\main.fga"
# path = r"D:\Files\1_Projects\Futsuga/"
# remove_comments(file, 'main_no_comments.fga')
parsed = parser2(file)#, path)
print(main_parser(parsed))
# print(f'{color.Fore.CYAN}{parsed}')
# print(remove_comments(file))

# with open("abc2.json", "w", encoding="utf-8") as f:
#     json.dump(parsed, f, ensure_ascii=False, indent=4)