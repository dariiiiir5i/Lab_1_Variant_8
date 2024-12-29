RED = '\u001b[41m'
GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'
END = '\u001b[0m'

for i in range(6):
    if i < 3:
        print(f'{GREEN}{"  " * 6}{YELLOW}{"  " * 10}{END}')
    else:
        print(f'{GREEN}{"  " * 6}{RED}{"  " * 10}{END}')