class pyfuncs:
    def print(*args, sep=' ', end='\n'):
        import io
        import sys

        output_buffer = io.StringIO()
        
        old_stdout = sys.stdout
        sys.stdout = output_buffer
        print(*args, sep=sep, end=end)
        sys.stdout = old_stdout
        
        result = output_buffer.getvalue()
        output_buffer.close()
        
        return result

    def input(value_type='int', prompt=''):
        txt = ''
        if prompt == '':
            txt += '\ninput();'