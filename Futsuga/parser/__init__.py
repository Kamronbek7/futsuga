from .constantas import *
from .functions  import *

import parser.parsers as parsers

# json data
main = {
    'init': {
        "TOKEN": "dotenv",
        "INLINE": True,
        "ADMIN_WARNINGS": True,
        "DATABASE_FILE": "dbs/main.db",
        "TELEGRAM_LOG": True,
        "LOGS": ["logs/{datetime}.log"]
    },
    "imports": {}
}

# Futsuga to JSON
def futs2json(file: str="D:/Files/1_Projects/Futsuga/Examples/sample_bot/main.fga"):
    n = 0
    fl = open('st.md', 'wb')
    fl.write(b'|Line|Turi|Data|\n|-|-|-|\n')
    old    = None
    header = None
    old_tab   = 0
    temp_line = ''
    for line in remove_comments(file).replace('|', '/./').split('\n'):
        n += 1
        res = ''
        if line.strip() == '': continue
        else:
            # asosiy natijalar
            res = how_code(line, old, header)
            if tab_counter(line) == 0: header = None

            # asosiy qism

            # yangi qator uchun tayyorlash
            old = res
            old_tab = int(res.split('.')[0])
            if 'begin' in res: header = res.split('.')[-1]

            # try:
            fl.write(f'|{n}|{res}|{line.strip()}|\n'.encode())
            # except Exception as e:
            #     print(e, line)
    fl.close()

if __name__ == '__main__':
    futs2json()