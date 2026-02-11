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

class init_params:
    admin_warnings = 'ADMIN_WARNINGS' # True
    admins         = 'ADMINS'         # [112, 80999]
    token    = 'TOKEN'       # .env
    webhook  = 'WEBHOOK'     # True/False
    database = 'DATABASE'    # None/File path
    inline   = 'INLINE'      # True - if webhook is not
    logs     = 'LOGS'        # telegram, logfile.log
    share    = 'SHARE'       # True/False (share some datas to futsuga server)
    parse    = 'PARSE'       # Usually, HTML. But maybe 'md'
    platform = 'PLATFORM'    # telegram (in the future discord, vk)
    compile  = 'COMPILE'     # False/True

class buttons:
    inline         = 'InlineButton'
    keyboard       = 'KeyboardButton'
    command_button = 'CommandButtons'

class file_handlers:
    file       = 'FILE'
    photo      = 'PHOTO'
    video      = 'VIDEO'
    video_note = 'VIDEO_NOTE'
    audio      = 'AUDIO'
    document   = 'DOCUMENT'

class_to_list = lambda name: tuple(eval(f'{name.__name__}.{i}') for i in dir(name) if '__' not in i)

functions = [i for i in dir(Bot) if (i[0]!='_' and (('send_' in i) or ('forward' in i)))]
functions.append('reply')

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