from parser import *

a = parsers.parse_commands('''

/start: "Botga xush kelibsiz"
/help: 'Siz /help\'ni bosdingiz'
/all:
	reply: 'Salom'
	send_message: "Xabar"

'''.strip())
import pprint
pprint.pprint(a, width=120)
# print(a)
