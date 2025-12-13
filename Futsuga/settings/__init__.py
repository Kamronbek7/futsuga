import sys

data = {
    "name": "Futsuga",
    "author": "Futsuga soft",
    "version": "v1.0.0a2",
    "fsg_version": "FSG version: v1.0.0",
    "langs": {
        "all": ["uzb", "eng"],
        "default": "eng"
    },
    "paths": {
        "windows": {
            "main": "%APPDATA%/$name$/"
        },
        "linux": {
            "main": "usr/bin/$name$/"
        },
        "macos": {},
        "all": {
            "packages": "$paths.system.main$/packages/",
            "site_packages": "$paths.packages$/site-packages/",
            "templates": "$paths.system.main$/templates/",
            "scripts": "$paths.system.main$/scripts/",
            "libs": "$paths.system.main$/libs/"
        }
    },
    "project": {
        "must": {
            "main": "src/main.fga",
            "settings_file": "src/settings.json",
            "env": ".env/",
            "token": ".env/.env",
            "proj": "project.toml",
            "database": {
                "main_dir": "dbs/",
                "users": "dbs/users.db"
            },
            "logs": {
                "main_dir": "logs/",
                "logs": "logs/data_$now$.log",
                "main_log_file": "logs/main.log"
            }
        }
    }
}

class datas:
    version = data['version']
    py_version = sys.version
    name = data['name']
    author = 'Kamronbek Quchqorov'
    langs = data['langs']['all']
    default_lang = data['langs']['default']
    fsg_version = data["fsg_version"]