import re
from collections import defaultdict

# AST tuzilmasi
class FutsugaAST:
    def __init__(self):
        self.config = {}
        self.commands = defaultdict(dict)
        self.texts = {}
        self.admin_panel = None
        self.files = {}
        self.keyboard_buttons = defaultdict(dict)
        self.inline_buttons = defaultdict(dict)

    def __str__(self):
        return (
            f"CONFIG: {self.config}\n\n"
            f"COMMANDS: {dict(self.commands)}\n\n"
            f"TEXTS: {self.texts}\n\n"
            f"ADMIN PANEL: {self.admin_panel}\n\n"
            f"FILES: {self.files}\n\n"
            f"KEYBOARD BUTTONS: {dict(self.keyboard_buttons)}\n\n"
            f"INLINE BUTTONS: {dict(self.inline_buttons)}"
        )

    def to_dict(self):
        return {
            "config": self.config,
            "commands": dict(self.commands),
            "texts": self.texts,
            "admin_panel": self.admin_panel,
            "files": self.files,
            "keyboard_buttons": dict(self.keyboard_buttons),
            "inline_buttons": dict(self.inline_buttons),
        }

# Parser funksiyasi
def parse_futsuga(code: str) -> FutsugaAST:
    if isinstance(code, bytes):
        code = code.decode("utf-8")

    lines = code.splitlines()
    ast = FutsugaAST()
    current_block = None
    sub_block = None
    command_key = None
    indent_stack = []

    def get_indent(line):
        return len(line) - len(line.lstrip())

    i = 0
    tr_counter = 1  # $tr uchun hisoblagich

    while i < len(lines):
        raw_line = lines[i]
        line = raw_line.strip()

        if line.startswith('#') or not line:
            i += 1
            continue

        # Bloklar boshida aniqlanadi
        match_block = re.match(r'^(\w+):$', line)
        if match_block:
            current_block = match_block.group(1)
            if current_block == "admin_panel":
                ast.admin_panel = True
            i += 1
            continue

        # Ichki sub-bloklar
        match_subblock = re.match(r'^(\w+)\s+(\w+):$', line)
        if current_block in ("KeyboardButtons", "InlineButtons") and match_subblock:
            _, sub_block = match_subblock.groups()
            i += 1
            continue

        # CONFIG
        if current_block == "config":
            key_match = re.match(r'^(\w+):$', line)
            if key_match:
                key = key_match.group(1)
                ast.config[key] = []
                indent_stack = [get_indent(raw_line)]
                i += 1
                while i < len(lines):
                    sub_line = lines[i]
                    if sub_line.strip().startswith('#') or not sub_line.strip():
                        i += 1
                        continue
                    if get_indent(sub_line) <= indent_stack[0]:
                        break
                    ast.config[key].append(sub_line.strip())
                    i += 1
                continue

            assign_match = re.match(r'^(\w+)\s*=\s*(.+)$', line)
            if assign_match:
                k, v = assign_match.groups()
                ast.config[k] = v.strip('"')

        # COMMANDS
        elif current_block == "commands":
            if line.endswith(':'):
                command_key = line[:-1]
                ast.commands[command_key]['body'] = []
            elif line.startswith('python:'):
                ast.commands[command_key]['body'].append('python:')
            else:
                ast.commands[command_key]['body'].append(line)

        # TEXT
        elif current_block == "text":
            if ':' in line:
                key, val = map(str.strip, line.split(':', 1))
                ast.texts[key.strip('~')] = val.strip('"')

        # FILES
        elif current_block == "files":
            if ':' in line:
                ftype, action = map(str.strip, line.split(':', 1))
                ast.files[ftype] = action.strip('"')

        # KeyboardButtons
        elif current_block == "KeyboardButtons" and sub_block:
            if '->' in line:
                label, cb = map(str.strip, line.split('->'))
                ast.keyboard_buttons[sub_block][label.strip('"')] = cb

        # InlineButtons
        elif current_block == "InlineButtons" and sub_block:
            if '->' in line:
                label, right = map(str.strip, line.split('->'))
                # maxsus $tr, $chat_name, $link o'rnini bosish
                label = label.replace("$tr", str(tr_counter))
                label = label.replace("$chat_name", "Channel")
                label = label.replace("$link", "https://example.com")

                if "$tr" in raw_line:
                    tr_counter += 1

                if right.startswith("link:"):
                    ast.inline_buttons[sub_block][label.strip('"')] = {"type": "link", "value": right[5:].strip()}
                elif right.startswith("callback_data:"):
                    ast.inline_buttons[sub_block][label.strip('"')] = {"type": "callback", "value": right[14:].strip()}
                else:
                    ast.inline_buttons[sub_block][label.strip('"')] = {"type": "unknown", "value": right.strip()}

        # keyboard_buttons_handler
        elif current_block == "keyboard_buttons_handler":
            if ':' in line:
                key, action = map(str.strip, line.split(':', 1))
                ast.keyboard_buttons[key] = action

        # inline_buttons_handler
        elif current_block == "inline_buttons_handler":
            if ':' in line:
                key, action = map(str.strip, line.split(':', 1))
                ast.inline_buttons[key] = action

        i += 1

    return ast

print(
    parse_futsuga(open(r"D:\\Files\\1_Projects\\Futsuga\\_excample\\src\\excample.fga", 'rb').read()).inline_buttons_handler
)
