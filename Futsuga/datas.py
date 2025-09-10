import sys, json

data = json.load(open('settings/datas.json'))
# print(data)
mydata = type('MyClass', (), data) #{'x': 42, 'foo': lambda self: self.x})
# print(mydata)
# print(mydata)

class datas:
    version = data['version']
    py_version = sys.version
    name = data['name']
    author = 'Kamronbek Quchqorov'
    langs = data['langs']['all']
    default_lang = data['langs']['default']
    fsg_version = data["fsg_version"]