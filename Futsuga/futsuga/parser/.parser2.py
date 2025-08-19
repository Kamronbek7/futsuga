import re

def parse_futsuga_to_dict(futsuga_code: str) -> dict:
    parsed = {
        'ADMINS': [],
        'TOKEN': '',
        'INLINE': False,
        'ADMIN_WARNINGS': False,
        'InlineButtons': {},
        'KeyboardButtons': {},
        'Commands': {},
        'TextTriggers': {},
        'CallbackData': {},
    }

    lines = futsuga_code.strip().split('\n')
    i = 0
    current_section = None
    current_key = None

    def extract_key_value(line):
        if '->' in line:
            key, val = line.split('->', 1)
            return key.strip('" '), val.strip()
        return None, None

    while i < len(lines):
        line = lines[i].strip()
        
        if line.startswith('ADMINS:'):
            i += 1
            while lines[i].strip() != '':
                parsed['ADMINS'].append(int(lines[i].strip(' ;')))
                i += 1
        elif line.startswith('TOKEN'):
            parsed['TOKEN'] = line.split(' ', 1)[1].strip()
        elif line.startswith('INLINE='):
            parsed['INLINE'] = line.split('=')[1].strip() == 'True'
        elif line.startswith('ADMIN_WARNINGS='):
            parsed['ADMIN_WARNINGS'] = line.split('=')[1].strip() == 'True'

        elif line.startswith('InlineButton'):
            _, name = line.replace(':', '').split()
            parsed['InlineButtons'][name] = []
            i += 1
            while i < len(lines) and lines[i].strip() != '':
                buttons = [s.strip() for s in lines[i].split('|') if s.strip()]
                row = []
                for btn in buttons:
                    key, val = extract_key_value(btn)
                    row.append((key, val))
                parsed['InlineButtons'][name].append(row)
                i += 1

        elif line.startswith('KeyboardButton'):
            _, name = line.replace(':', '').split()
            parsed['KeyboardButtons'][name] = []
            i += 1
            while i < len(lines) and lines[i].strip() != '':
                key, val = extract_key_value(lines[i])
                parsed['KeyboardButtons'][name].append((key, val))
                i += 1

        elif re.match(r'^/[a-zA-Z_]+:', line):
            cmd = line.split(':')[0]
            parsed['Commands'][cmd] = []
            i += 1
            while i < len(lines) and lines[i].strip() != '':
                parsed['Commands'][cmd].append(lines[i].strip())
                i += 1

        elif line.startswith('/help'):
            cmd, msg = line.split(' ', 1)
            parsed['Commands'][cmd] = [f'reply {msg.strip()}']

        elif line.startswith('~"'):
            text = re.search(r'~"(.*?)"', line).group(1)
            message = re.search(r'"(.*?)"', line.split(text)[-1]).group(1)
            buttons = re.search(r'reply_buttons=(\\w+)', line)
            parsed['TextTriggers'][text] = {
                'reply': message,
                'reply_buttons': buttons.group(1) if buttons else None
            }

        elif line.startswith('callback_data:'):
            i += 1
            while i < len(lines):
                l = lines[i].strip()
                if l == '':
                    break
                if ':' in l:
                    key, val = l.split(':', 1)
                    key = key.strip()
                    val = val.strip()
                    if val in ['delete', 'show_alert "Sizga ham xayr"']:
                        parsed['CallbackData'][key] = val
                    elif val == 'verify:':
                        parsed['CallbackData']['verify'] = {}
                        i += 1
                        while i < len(lines) and lines[i].strip().startswith('#') is False:
                            subline = lines[i].strip()
                            if ':' in subline:
                                subkey, subval = subline.split(':', 1)
                                parsed['CallbackData']['verify'][subkey.strip()] = subval.strip(' "')
                            elif '"' in subline:
                                parsed['CallbackData']['verify']['message'] = subline.strip(' "')
                            elif 'reply_buttons=' in subline:
                                parsed['CallbackData']['verify']['reply_buttons'] = subline.split('=')[-1]
                            i += 1
                        continue
                i += 1
        else:
            i += 1

    return parsed

def parse_futsuga_to_dict(futsuga_code: str) -> dict:
    futsuga_code = futsuga_code.decode()
    parsed = {
        'ADMINS': [],
        'TOKEN': '',
        'INLINE': False,
        'ADMIN_WARNINGS': False,
        'InlineButtons': {},
        'KeyboardButtons': {},
        'Commands': {},
        'TextTriggers': {},
        'CallbackData': {},
    }

    lines = futsuga_code.strip().split('\n')
    i = 0

    def extract_key_value(line):
        if '->' in line:
            key, val = line.split('->', 1)
            return key.strip('" '), val.strip()
        return None, None

    while i < len(lines):
        line = lines[i].strip()

        if line.startswith('ADMINS:'):
            i += 1
            while i < len(lines):
                stripped = lines[i].strip()
                if not stripped or stripped.startswith('#') or not stripped[0].isdigit():
                    break
                try:
                    parsed['ADMINS'].append(int(stripped.strip(' ;')))
                except ValueError:
                    break
                i += 1
            continue

        if line.startswith('TOKEN'):
            parsed['TOKEN'] = line.split(' ', 1)[1].strip()

        elif line.startswith('INLINE='):
            parsed['INLINE'] = line.split('=')[1].strip() == 'True'

        elif line.startswith('ADMIN_WARNINGS='):
            parsed['ADMIN_WARNINGS'] = line.split('=')[1].strip() == 'True'

        elif line.startswith('InlineButton'):
            _, name = line.replace(':', '').split()
            parsed['InlineButtons'][name] = []
            i += 1
            while i < len(lines) and lines[i].strip() != '' and not lines[i].startswith('#'):
                buttons = [s.strip() for s in lines[i].split('|') if s.strip()]
                row = []
                for btn in buttons:
                    key, val = extract_key_value(btn)
                    row.append((key, val))
                parsed['InlineButtons'][name].append(row)
                i += 1
            continue

        elif line.startswith('KeyboardButton'):
            _, name = line.replace(':', '').split()
            parsed['KeyboardButtons'][name] = []
            i += 1
            while i < len(lines) and lines[i].strip() != '' and not lines[i].startswith('#'):
                key, val = extract_key_value(lines[i])
                parsed['KeyboardButtons'][name].append((key, val))
                i += 1
            continue

        elif re.match(r'^/[a-zA-Z_]+:', line):
            cmd = line.split(':')[0]
            parsed['Commands'][cmd] = []
            i += 1
            while i < len(lines) and lines[i].strip() != '' and not lines[i].startswith('#'):
                parsed['Commands'][cmd].append(lines[i].strip())
                i += 1
            continue

        elif line.startswith('/help'):
            cmd, msg = line.split(' ', 1)
            parsed['Commands'][cmd] = [f'reply {msg.strip()}']

        elif line.startswith('~"'):
            text = re.search(r'~"(.*?)"', line).group(1)
            message = re.search(r'"(.*?)"', line.split(text)[-1]).group(1)
            buttons = re.search(r'reply_buttons=(\w+)', line)
            parsed['TextTriggers'][text] = {
                'reply': message,
                'reply_buttons': buttons.group(1) if buttons else None
            }

        elif line.startswith('callback_data:'):
            i += 1
            while i < len(lines):
                l = lines[i].strip()
                if l == '':
                    break
                if ':' in l:
                    key, val = l.split(':', 1)
                    key = key.strip()
                    val = val.strip()
                    if val in ['delete', 'show_alert "Sizga ham xayr"']:
                        parsed['CallbackData'][key] = val
                    elif key == 'verify':
                        parsed['CallbackData']['verify'] = {}
                        i += 1
                        while i < len(lines) and lines[i].strip().startswith('#') is False:
                            subline = lines[i].strip()
                            if ':' in subline:
                                subkey, subval = subline.split(':', 1)
                                parsed['CallbackData']['verify'][subkey.strip()] = subval.strip(' "')
                            elif '"' in subline:
                                parsed['CallbackData']['verify']['message'] = subline.strip(' "')
                            elif 'reply_buttons=' in subline:
                                parsed['CallbackData']['verify']['reply_buttons'] = subline.split('=')[-1]
                            i += 1
                        continue
                i += 1
        i += 1

    return parsed