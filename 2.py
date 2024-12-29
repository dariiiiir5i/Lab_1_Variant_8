BLACK = '\u001b[40m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

for i in range(7):
        if i < 3:
            print(f'{WHITE}{"  "  * ((10 - ( i * 2 + 2 )) // 2) }{BLACK}{"  "  * ( i * 2 + 2 ) }{WHITE}{"  "  * ( 7 - ( i * 2 + 2 )) }{BLACK}{"  "  * ( i * 2 + 2 ) }{WHITE}{"  "  * ( 4 - i ) }{END}')
        elif i==3:
            print(f'{WHITE}{"  "  * ((10 - ( i * 2 + 2 )) // 2) }{BLACK}{"  "  * ((( i * 2 + 2 ) * 2) - 1) }{WHITE}{"  "  * ((10 - ( i * 2 + 2 )) // 2) }{END}')
        else:
            print(f'{WHITE}{"  "  * (i - 2)}{BLACK}{"  "  * (14 - ( 2 * i ))}{WHITE}{"  "  * (((i-3)*2)-1)}{BLACK}{"  "  * (14 - ( 2 * i ))}{WHITE}{"  "  * (i-2)}{END}')
