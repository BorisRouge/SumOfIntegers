import re
import pprint
from count import count_1, count_2


def start():
    while True:
        n = input('Введите количество клиентов и, '
                  'если необходимо, первый ID в последовательности:\n')
        if not re.search(r'^ *\d[\d ]*$', n):
            print('Аргументы должны содержать только цифры.')
        else:
            args = n.split(' ')
            if len(args) > 2:
                print('Слишком много аргументов. Попробуйте еще раз.')
            else:
                try:
                    result = count_2(int(args[0]), int(args[1]))
                except IndexError:
                    result = count_1(int(args[0]))
                print('Число покупателей, попадающих в каждую группу:')
                pprint.pprint(result)
                break


start()
