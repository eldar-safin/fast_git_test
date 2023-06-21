#!/usr/bin/env python3
import sys
import re

methods_list = ['сложение', 'вычитание', 'умножение', 'деление']


def calculate(a, b, method):
    if method == 'сложение':
        result = a + b
    elif method == 'вычитание':
        result = a - b
    elif method == '*':
        result = a * b
    elif method == 'деление':
        if b == 0:
            return None, 'Попытка делить на ноль'
        result = int(a / b)
    else:
        return None, 'Неизвестный метод'
    return result, None


def main():
    a = int(input('Введите первое число:'))
    print()
    b = int(input('Введите второе число:'))
    print()
    print('Доступные методы:')
    for i, item in enumerate(methods_list):
        print(f'[{i}] {item}')
    method_num = input('Введите число [0]:')
    if not method_num:
        method_num = 0
    method = methods_list[int(method_num)]
    result, error = calculate(a, b, method)
    if error:
        print('Ошибка:', error)
        exit(1)
    else:
        print('Результат:', result)


if __name__ == '__main__':
    filename = sys.argv[0]
    target_pattern = re.compile(r'^(?P<a>\d*)(?P<method>[\*\+\-\/]?)(?P<b>\d*)$')
    first_message = 'Simple calc 0.0'
    help_message = f'See "{filename} --help".'

    for ind in range(1, len(sys.argv)):
        arg = sys.argv[ind]
        arg_target = re.match(target_pattern, arg)
        if arg_target and all(arg_target.groups()):
            result, error = calculate(**arg_target.groupdict())
            if error:
                print('Ошибка:', error)
                exit(1)
            else:
                print('Результат:', result)
        else:
            if arg == '-h' or arg == '--help':
                print(first_message)
                print(f'Usage: python3 {filename} [options] [target] ...\n')
                print('Options:\n')
                print('\t-h, --help\tPrint this message and exit.')
                print('\t-v, --version\tPrint the version number of make and exit.')
                exit()
            elif arg == '-v' or arg == '--version':
                print(first_message)
                print(help_message)
            else:
                print('Unknown flag:', arg)
                print(help_message)
                exit(1)
    # main()
