# A. Задана натуральная степень k.

import random

def file_text(str):
    with open('pol.txt', 'w') as data:
        data.write (str)

def gen_random():
    return random.randint(0, 101)

def funcktoin_a(k):
    a = [gen_random() for i in range(k+1)]
    return a

def function_create(s):
    lst = s[::-1]
    w = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                w += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    w += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                w += f'{lst[i]}x'
                if lst[i+1] != 0:
                    w += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                w += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                w += ' = 0'
    return w


k = int(input("Введите k = "))
kof = funcktoin_a(k)
file_text(function_create(kof))