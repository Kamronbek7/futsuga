from sys import exit

def prex(text, error_code=1):
    return text
    exit(error_code)

class MainErrors:
    def __init__(self, line, text, file, **kw):
        """
        101 - SyntaxError
        102 - IndentationError
        103 - TabError
        """
        self.error_code = 100
        self.text = text
        self.line = line
        self.file = file
        self.kw = kw
        self.text = f'File: {file!a}\t\tLine: {line}\n'
    
    def SyntaxError(self):
        return self.text + f'SyntaxError: {self.text}', self.error_code + 1

    def IndentationError(self):
        pass

class Main2Errors:
    """
    201 - NameError
    """
    def NameError(self):
        pass

class FileSystemErrors:
    """
    301 - FileNotFoundError
    302 - IsADirectoryError
    303 - FileExistsError
    """
    pass

class BotErrors:
    pass

# exit(303)