import os
os.chdir(os.path.dirname(__file__))
# changing workind directory to dir of file, because working dir can differ from path to script file
"""
Чайковський Павло 125Б
а) Дан текстовий файл f. Переписати у файл g всі рядки з вихідного файлу, в кінці
кожного рядка додавши знак оклику (!).
б) Дано текстові файли f і g. Записати в файл h спочатку компоненти файлу f, потім
- компоненти файлу g зі збереженням порядку.
"""

from string import ascii_letters, digits
from random import choice, randint as rd
chars = ascii_letters + digits
import pprint

def write_lines(file, Print=False):
    with open(file, 'w') as f_write:
        # 15 rows, from 10 to 50 characters in each
        random_strings = '\n'.join([''.join([choice(chars) for i in range(10, rd(10,50))]) for j in range(15)])
        if Print:
            pprint.pprint(random_strings)
        f_write.writelines(random_strings)

def writeFilesToFile(*args, char="!"):
    # last filename is that file we want to write to
    for i in args[0:-1]:
        flag = 'w' if args.index(i) == 0 else 'a'
        with open(i, 'r') as file_1_read, open(args[-1], flag) as file_2_write:
            lines = [i.replace('\n', f'{char}\n') for i in file_1_read.readlines()]
            lines[-1] = lines[-1] + char
            file_2_write.writelines(lines)

def printFileContent(file):
    with open(file, 'r') as f:
        pprint.pprint(f.readlines())

def a_task():
    write_lines('f')
    writeFilesToFile('f', 'g', char="!")
    printFileContent('g')

def b_task():
    write_lines('f')
    write_lines('g')
    writeFilesToFile('f', 'g', 'h')

if __name__ == '__main__':
    while True:
        c = input('What task? a/b: ').strip()
        if c in ('a', 'b'):
            break
    if c == 'a':
        a_task()
    elif c == 'b':
        b_task()
