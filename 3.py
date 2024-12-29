BLACK = '\u001b[40m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

for i in range(10):
        if i < 9:
            print(f'{9-i}{" | "}{WHITE}{"  "  * ( 8 - i ) }{BLACK}{"  "  * 1 }{WHITE}{"  "  * ( i + 1 ) }{END}')
        else:
            print(f'{"0 | "}{WHITE}{"  "  * (i + 1) }{END}')
