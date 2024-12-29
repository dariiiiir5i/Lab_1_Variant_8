RED = '\u001b[41m'
GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'
BLACK = '\u001b[40m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

file = open('sequence.txt', 'r')
list_plus = []
list_minus = []
for number in file:
    if float(number) > 0 and float(number) < 5:
        list_plus.append(number)
    if float(number) < 0 and float(number) > -5:
        list_minus.append(number)
len_plus = len(list_plus)
len_minus = len(list_minus)
proc_pl = ((len_plus / (len_plus + len_minus)) * 100)
proc_min = ((len_minus / (len_plus + len_minus)) * 100)
print(f'{END}')
print(f'{GREEN}{"  "}{BLACK}{" От -5 до 0 | кол-во: "}{len_minus}{" | процентное соотношение: "}{round(proc_min , 1)}{" %"}{END}')
print(f'{RED}{"  "}{BLACK}{" От 0 до 5 | кол-во: "}{len_plus}{" | процентное соотношение: "}{round(proc_pl , 1)}{" %"}{END}')
print(f'{round(proc_min , 1)}{" % "}{GREEN}{"  " * int(proc_min // 10)*2}{RED}{"  " * int(proc_pl// 10)*2}{BLACK}{" "}{round(proc_pl , 1)}{" %"}{END}')
file.close()