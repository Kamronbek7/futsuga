def get_default_lang():
    import datas as a
    return a.datas.default_lang

def take_data(text_id, lang=get_default_lang(), tp='errors'):
    from sqlite3 import connect
    a = connect('langs/langs.db')
    c = a.cursor()
    c.execute(f'SELECT {lang} FROM {tp} WHERE word == "{text_id}"')
    data = c.fetchall()
    a.close()
    return str(data[0][0])

def read_data(text_id, lang=get_default_lang(), tp='errors', **kwargs):
    data = take_data(text_id=text_id, lang=lang, tp=tp)
    for i in kwargs['kwargs']:
        data = data.replace(i, kwargs['kwargs'][i])
    return data