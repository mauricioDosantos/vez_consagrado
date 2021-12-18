from time import sleep
from os import get_terminal_size, system

def main():
    print('----------┐  ┌----------  :          :  ┌----------')
    print('|         |  |            |          |  |          ')
    print('|         |  |            |          |  |          ')
    print('|         |  ├-----       |          |  └---------┐')
    print('|         |  |            |          |            |')
    print('|         |  |            |          |            |')
    print('----------┘  └----------  └----------┘  ----------┘')
    print('                                      ___________  ')
    print(r'\          /  |          |  |             |      |')
    print(r' \        /   |          |  |             |      |')
    print(r'  \      /    |          |  |             |      |')
    print(r'   \    /     |          |  |             |      |')
    print(r'    \  /      |          |  |             |      |')
    print(r'     \/       └----------┘  └--------     |      ▀')


    def deus(i):
        print(' ' * i, '-' * 10 + '┐' + ' ' * 2 + '┌' + '-' * 10, end='')
        print(' ' * 2 + ':' + ' ' * 10 + ':' + ' ' * 2 + '┌' + '-' * 11)

        # segunda linha
        print(' ' * i, '|' + ' ' * 9 + '|' + ' ' * 2 + '|' + ' ' * 12, end='')
        print('|', ' ' * 9 + '|' + ' ' * 2 + '|')

        # terceira linha
        print(' ' * i, '|' + ' ' * 9 + '|' + ' ' * 2 + '|' + ' ' * 12, end='')
        print('|', ' ' * 9 + '|' + ' ' * 2 + '|')

        # quarta linha
        print(' ' * i, '|         ', end='|  ')
        print('├-----', end=' ' * 7)
        print('|', ' ' * 9, end='|')
        print('  └' + ('-' * 9) + '┐')

        # quinta linha
        print(' ' * i, '|' + ' ' * 9 + '|' + ' ' * 2 + '|' + ' ' * 12, end='')
        print('|', ' ' * 9 + '|' + ' ' * 12 + '|')

        # sexta linha
        print(' ' * i, '|' + ' ' * 9 + '|' + ' ' * 2 + '|' + ' ' * 12, end='')
        print('|', ' ' * 9 + '|' + ' ' * 12 + '|')

        # sétima linha
        print(' ' * i, '-' * 10 + '┘' + ' ' * 2 + '└' + '-' * 10 + ' ' * 2, end='')  # D e E
        print('└' + '-' * 10 + '┘' + ' ' * 2 + '-' * 10 + '┘')  # U e S


    def vult(i):
        # primeira linha VULT!
        print(' ' * i + ' ' * 38 + '_' * 13)

        # segunda linha VULT!
        print(
            ' ' * i + '\ ' + ' ' * 9 + '/' + ' ' * 2 + '|' + ' ' * 10 + '|' + ' ' * 2 + '|' + ' ' * 13 + '|' + ' ' * 6 + '|')

        # terceira linha VULT!
        print(
            ' ' * i + ' ' + '\ ' + ' ' * 7 + '/' + ' ' * 3 + '|' + ' ' * 10 + '|' + ' ' * 2 + '|' + ' ' * 13 + '|' + ' ' * 6 + '|')

        # quarta linha VULT!
        print(
            ' ' * i + ' ' * 2 + '\ ' + ' ' * 5 + '/' + ' ' * 4 + '|' + ' ' * 10 + '|' + ' ' * 2 + '|' + ' ' * 13 + '|' + ' ' * 6 + '|')

        # quinta linha VULT!
        print(
            ' ' * i + ' ' * 3 + '\ ' + ' ' * 3 + '/' + ' ' * 5 + '|' + ' ' * 10 + '|' + ' ' * 2 + '|' + ' ' * 13 + '|' + ' ' * 6 + '|')

        # sexta linha VULT!
        print(
            ' ' * i + ' ' * 4 + '\ ' + ' ' * 1 + '/' + ' ' * 6 + '|' + ' ' * 10 + '|' + ' ' * 2 + '|' + ' ' * 13 + '|' + ' ' * 6 + '|')

        # sétima linha VULT!
        print(
            ' ' * i + ' ' * 5 + r'\/' + ' ' * 7 + '└' + '-' * 10 + '┘' + ' ' * 2 + '└' + '-' * 8 + ' ' * 5 + '|' + ' ' * 6 + '▀')


    var = get_terminal_size()  # pega o tamanho do terminal, esta função retorna uma tupla(colunas,linhas)
    quantidade = var[0] - 53  # margem de erro de +2
    while True:
        for i in range(quantidade):
            system('cls')
            deus(i)
            vult(i)

            sleep(0.5)

        for e in range(quantidade, 0, -1):
            system('cls')
            deus(e)
            vult(e)

            sleep(0.5)
