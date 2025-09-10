from telegram import Bot
body = [
    'init',
    'imports',
    'InlineButtons',
    'KeyboardButtons',
    'commands',
    'text',
    'admin_panel',
    'files',
    'keyboard_buttons_handler',
    'inline_buttons_handler',
    'chat_handlers'
]

class params:
    admin_warnings = 'admin_warnings'.upper()
    admins   = 'ADMINS'
    token    = 'TOKEN'
    webhook  = 'WEBHOOK'
    database = 'DATABASE'
    inline   = 'INLINE'
    logs     = 'LOGS'
    share    = 'SHARE'

class buttons:
    inline         = 'InlineButton'
    keyboard       = 'KeyboardButton'
    command_button = 'CommandButtons'

class file_handlers:
    file       = 'FILE'
    photo      = 'PHOTO'
    video      = 'video'.upper()
    video_note = 'video_note'.upper()
    audio      = 'AUDIO'
    document   = 'DOCUMENT'

class_to_list = lambda name: tuple(eval(f'{name.__name__}.{i}') for i in dir(name) if '__' not in i)

# a = 'to_json to_dict de_json de_list close'.split(' ')
functions = [i for i in dir(Bot) if (i[0]!='_' and (('send_' in i) or ('forward' in i)))]
functions.append('reply')
# functions.remove('to_json')
# functions.remove('to_dict')
# functions.remove('de_json')
# functions.remove('de_list')
# functions.remove('close')

# b = 'create, delete, send, set, get, verify, unban, unpin, leave, hide, pin, transfer, remove, reopen, restrict, refund, promote, post, read, add, ban, base_url, bot, can, close, convert, copy, decline, edit, forward, restrict, save, username, id, link, name'.split(', ')
# for i in functions:
#     for j in b:
#         if not j in i or not '_' in i:
#             try:
#                 functions.remove(i)
#                 print(i)
#             except: pass#rint(i, '\t\t', i, j)

libraries = [
    'uzbeksila',
    'futsuga_ads',
    'admin_panel',
    'download'
]

if __name__ == '__main__':
    n = 0
    for i in functions:
        n += 1
        print(i.ljust(50), end='')
        if n == 5:
            print()
            n = 0