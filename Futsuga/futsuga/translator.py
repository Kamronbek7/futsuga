from parser import *
from parser.functions import tab_counter
from parser import parsers

class Transpiler:
    def __init__(self):
        self.list_data = ''
        self
        self.messagehandlers  = '# Message Handlers\n'
        self.commandhandlers  = '# Command Handlers\n'
        self.commandfunctions = '# Functions for Commands\n'
        
    def init(self, json) -> str:
        code = ''
        for value in json:
            code += f'\t{value} = {json[value]!a}\n'
        if not 'TOKEN' in json:
            pass
        return code

    '''def commands(self, json) -> None:
        for code in json:

            self.commandhandlers  += f'CommandHandler({code!a}, {code}_func)\n'
            if not isinstance(json[code], list):
                self.commandfunctions += f'\nasync def {code}_func(update, context):\n\tawait update.message.{code}({json[code]!a})\n'

            # if   isinstance(json[code], list):
                self.commandfunctions += f'\nasync def {code}_func(update, context):\n'
                for commands in json[code]:
                    for command in commands:
                        # print(f'{json[code] = }\n{commands = }\n{command = }')
                        self.commandfunctions += f'\tawait {command}({commands[command]!a})\n'

            elif isinstance(json[code],  str):
                # print(json[code])
                value = json[code]
                self.commandfunctions += f'\t{code}({value!r})\n'
                # print(self.commandfunctions, '='*20)'''
    
    def commands(self, commands_dict):
        functions_code = []
        handlers_code = []
        
        for command_name, actions in commands_dict.items():
            function_name = f"{command_name}_function"
            
            # Function body yaratish
            function_lines = []
            function_lines.append(f"async def {function_name}(update, context):")
            
            for action in actions:
                func_type = action['function']
                text = action['text'].replace('"', '\\"').replace("'", "\\'")
                
                if func_type == 'reply':
                    function_lines.append(f"\tawait update.message.reply_text(\"{text}\")")
                elif func_type == 'send_message':
                    function_lines.append(f"\tawait context.bot.send_message(chat_id=update.effective_chat.id, text=\"{text}\")")
                else:
                    function_lines.append(f"\t# Noma'lum funksiya: {func_type}")
                    function_lines.append(f"\tawait update.message.reply_text(\"{text}\")")
            
            functions_code.append("\n".join(function_lines))
            
            # Handler code yaratish
            handler_code = f"app.add_handler(CommandHandler('{command_name}', {function_name}))"
            handlers_code.append(handler_code)
        self.commandfunctions = "\n\n".join(functions_code)
        self.commandhandlers  = "\n"  .join( handlers_code)
        
        return "\n\n".join(functions_code), "\n".join(handlers_code)
    
    def parse_config(self, text):
        lines = text.strip().split('\n')
        
        init_config = {}
        commands_text = []
        in_init_section = False
        in_commands_section = False
        
        for line in lines:
            line = line.strip()
            
            if line == 'init:':
                in_init_section = True
                in_commands_section = False
                continue
            elif line.startswith('/'):
                in_init_section = False
                in_commands_section = True
            
            if in_init_section and line and ':' in line:
                # Init bo'limini qayta ishlash
                parts = line.split(':', 1)
                key = parts[0].strip()
                value = parts[1].strip().strip('"\'')
                
                # LOG qiymatini boolean ga o'girish
                if key == 'LOG':
                    value = value.lower() == 'true'
                
                init_config[key] = value
            
            elif in_commands_section and line:
                # Buyruqlar bo'limini saqlash
                commands_text.append(line)
        
        # Buyruqlar matnini birlashtirish
        commands_full_text = '\n'.join(commands_text)
        
        return init_config, commands_full_text
    
    def section_cutter(self, code):
        lines = code.split('\n')
        init_lines = []
        commands_lines = []
        is_init_section = False
        is_commands_section = False

        for line in lines:
            if line.strip() == 'init:':
                is_init_section = True
                is_commands_section = False
                init_lines.append(line)
            elif line.startswith('/'):
                is_init_section = False
                is_commands_section = True
                commands_lines.append(line)
            elif is_init_section:
                init_lines.append(line)
            elif is_commands_section:
                commands_lines.append(line)

        init = '\n'.join(init_lines)
        commands = '\n'.join(commands_lines)
        return init, commands

    def messages(self, json) -> None:
        pass

class ToPython:
    def __init__(self, futs_code):
        self.futs_code = futs_code
        self.     code = f'''import warnings
from telegram.warnings import PTBUserWarning

warnings.filterwarnings("ignore", category=PTBUserWarning)

from telegram.ext import (
\tCommandHandler,
\tMessageHandler,
\tfilters,
\tApplicationBuilder
)
from telegram import (
\tBot,
\tReplyKeyboardMarkup,
\tInlineKeyboardButton,
\tInlineKeyboardMarkup,
\tReplyKeyboardMarkup,
\terror
)

class constantas:
\thtml = "HTML"
\t# bot = Bot()\n
'''
        self.python = ''

        init_config, commands_text = Transpiler().section_cutter(futs_code)
        # print(init_config)
        json_init     = parsers.init_parser(init_config)
        json_commands = parsers.parse_commands(commands_text)

        py_init = Transpiler().init(json_init)
        py_commands, py_com_funcs = Transpiler().commands(json_commands)

        self.py_init     = py_init
        self.commandfunctions = py_com_funcs
        self.commandhandlers  = py_commands

    def get_python(self) -> str:
        return self.code + f"""{self.py_init}

# Main part
app = ApplicationBuilder().token(constantas.TOKEN).build()

# Command functions
{self.commandhandlers}

# Command handlers
{self.commandfunctions}

# self.messagehandlers

try: app.run_polling()
except error.NetworkError: print("Connection is no")
except Exception as e: print(e)
"""
    
def Futsuga(file):
    pass

if __name__ == '__main__':
    from parser import remove_comments

    code = remove_comments("""
/start: "Botga xush kelibsiz"
/help: 'Siz /help\'ni bosdingiz'
/all:
	reply: 'Salom'
	send_message: "Xabar"
""")
    py = ToPython(code)
    print(py.get_python())
