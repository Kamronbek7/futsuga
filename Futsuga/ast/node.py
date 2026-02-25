class InitNode:
    def __init__(self,
        token,
        inline=True,
        admin_warnings=True,
        database='sqlite3|dbs/'
):
        self.TOKEN = token
        self.inline = inline
        self.admin_warnings = admin_warnings
        self.database = database