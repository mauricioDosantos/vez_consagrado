#-*- coding utf-8 -*-

#import pyautogui
#https://pyautogui.readthedocs.io/en/latest/screenshot.html
#from platform import system as pf_sys
#from os import O_SEQUENTIAL, cpu_count, system
from time import sleep
#from typing import Literal
from DEUS_VULT import main as vult
#from keyboard import read_key

#choice = lambda dict_: [key for key,value in dict_ if locals() < value]
#counter = lambda gp, dict_: [print(valuel) + value for valuel in locals() if valuel is type(1) for value in dict_.values()]


def priorization_print(data):
    print('\n--------- Distribuição dos pontos ----------')
    for key, valeu in data.items():
        space = 29 - len(key) #44 - 4{igual dois digítos}
        print(key,' '*space,'| ',valeu['points'])
    print(f'Total: {counter(data)}\n')


def generate_csv(data):
    print('Gerando csv....')
    sleep(1)
    with open('priorização.csv','w+',encoding='utf-8') as file:
        file.write('Priorizador|Pontos\n')
        for key,value in data.items():
            val_ = value['points']
            file.write(f'{key}|{val_}\n')
    
    print('Arquivo salvo no mesmo diretório do arquivo')


def choice(dict_):
    if not dict_:
        return

    min_ = {'name': 'alguem','points':999}
    min_order = 999
    for key, value in dict_.items():

        if value['points'] <= min_['points'] and value['order'] < min_order:
            min_['points'] = value['points']
            min_['name'] = key
            min_order = value['order']

        elif value['points'] < min_['points']:
            min_['points'] = value['points']
            min_['name'] = key

    return min_


def counter(dict_):
    count = 0
    for key, value in dict_.items():
        count += value['points']
    return count


def all_are_the_same(play_order):
    count = 0
    for v in play_order:
        for v_2 in play_order:
            if v == v_2:
                count += 1
        break
    
    if count == len(play_order):
        return True
    else:
        return False


def equal_all(dict_):
    result = None
    for v in dict_.values():
        for v_2 in dict_.values():
            if v['points'] == v_2['points']:
                result = True
            else:
                return False
        break
    return result


def point_min(squad):
    min_ = 999
    min_order = 999
    for k, v in squad.items():
        if v['points'] <=  min_ and v['order'] < min_order:
            min_ = v['points']
            name = k
            min_order = v['order']
        
    return name


def priorization_order(squad):

    squad_copy = squad.copy()
    count = 0

    while len(squad) - 1:

        if equal_all(squad_copy):

            squad[point_min(squad_copy)]['order'] = count
            squad_copy.pop(point_min(squad_copy))
        else:

            min_ = choice(squad_copy)
            if not min_:
                return squad
            squad_copy.pop(min_['name'])
            squad[min_['name']]['order'] = count
        
        count += 1

    return squad


def get_max_val(squad):

    _max_val = {'name': 'alguem','points':-1}
    for k, v in squad.items():
        if v['active_round']:
            if v['points'] > _max_val['points']:
                _max_val['name'] = k
                _max_val['points'] =  v['points']

    if _max_val['points'] == -1:
        _max_val = None

    return _max_val

#in progress
def att_status(squad,count):
    marge_min = 4
    print(squad)
    while True:

        _min = choice(squad)
        _max = get_max_val(squad)
        print(_max)
        if _max == None:
            break

        if (_max['points'] - _min['points']) >= marge_min:
            squad[_max['name']]['order'] = count - 1 if count >= 1 else count + 1
        print(squad)
    return squad

# ordenar por pontos, se nomes iguais último que pediu
def prioritization(squad,general_points):
    
    round = 1
    count = 0
    squad = priorization_order(squad)
    print(squad)
    
    while counter(squad) < general_points:
        print(counter(squad))

        if len(squad) == count:

            squad = priorization_order(squad)
            count = 0
            round += 1
    #in progress
        #squad = att_status(squad, count)
        player = ''.join([k for k,v in squad.items() if count == v['order'] and v['active_round']])
        if player == '':
            count += 1
            continue

        #clean_terminal()
        priorization_print(squad)
        print(f'Rodada de número {round}')
        print('Pular priorização -1  ||  Deixar de priorizar -2 || Alterar pontos da sprint -3')
        print(f'Vez do(a) consagrado(a) {player}. Quantos pontos irá subir nessa rodada?')
        value = input_values()

        if value == -1:

            print('\n',list(squad.keys()))
            print('Em quem deve ser adicionados pontos?')
            people = input().strip().capitalize()
            while people not in squad.keys():
                print('Em quem deve ser adicionados pontos?')
                people = input().strip().capitalize()

            print('Quantos pontos serão acrescentados?')
            squad[people]['points'] += input_values()
            squad[people]['order'] = count

            count += 1

        elif value == -2:

            print('\n',list(squad.keys()))
            print('Quem irá sair?')
            people = input().strip().capitalize()

            while people not in squad.keys():
                print('Quem irá sair?')
                people = input().strip().capitalize()

            squad[people]['active_round'] = False

        elif value == -3:

            #clean_terminal()
            print(f'Quantidade de pontos definida é {general_points}')
            print('Qual a nova quantidade de pontos?')
            general_points = input_values()

        else:
            squad[player]['points'] += value
            squad[player]['order'] = count
            count += 1

    return squad, general_points


def input_values(type_='i'):
    """
    type_ = s strings
    type_ = i integer
    """
    if type_ == 'i':
        value = ''
        while type(value) != int:
            try:
                value = int(input())
            except ValueError:
                print('Que valor é esse? Oxente. Digite certo homi(muié).')
        return value


def main():
    print('Uma vez me perguntaram....')
    sleep(2)
    #clean_terminal()
    print('...... De quem é a vez do consagrado? ......')
    squad = {}

    print('Qual o nome da sprint?')
    sprint_name = input().capitalize()
    print(f'\nQuantos pontos a sprint {sprint_name} terá?')
    general_points = input_values()

    print('\nEscolha uma opção que contenha todos os que irão pontuar na sprint')
    print('\n---------------- Opções ------------------')
    print('1- Caio Ribeiro, Ramon Gouvea, Maria Amália, Ana Paula, Lucas Leandro, Gabriel Melo, Jucélio Fernandes')
    print('2- Caio Ribeiro, Ramon Gouvea, Lucas Leandro, Jucélio Fernandes, Maria Amália, Ana Paula')
    print('3- Caio Ribeiro, Ramon Gouvea, Erimar, Jucélio Fernandes')
    print('4- Criar própria lista')
    op = input().strip()
    
    if op == '1':
        peoples = ['Caio Ribeiro','Ramon Gouvea','Maria Amália','Ana Paula','Lucas Leandro','Gabriel Melo','Jucélio Fernandes']
    elif op == '2':
        peoples = ['Caio Ribeiro','Ramon Gouvea','Lucas Leandro','Jucélio Fernandes', 'Maria Amália', 'Ana Paula']
    elif op == '3':
        peoples = ['Caio Ribeiro','Jucélio Fernandes', 'Ramon Gouvea', 'Erimar']
    elif op == '4':
        print(f'Quem são os participantes da sprint {sprint_name}?(separado por vírgula, Ex: alguém, alguém)')
        peoples = input().split(',')

    count = 0
    #creating initial fase of squad dictionary 
    for valor in peoples:
        
        valor = valor.strip()
        valor = valor.capitalize()
        print(f'\nQuantos pontos tem o(a) {valor}?')
        
        squad[valor] = {'points': input_values(),'active_round':True, 'order': count}
        count += 1
    
    initial_fase = squad.copy()

    squad, general_points = prioritization(squad,general_points)

    while True:
        #clean_terminal()
        print('---------------- Opções ------------------')
        print('1- Tirar pontos   2- Finalizar e gerar csv')
        print('3- Apenas sair    4- Total de pontos')
        print('5- Repriorizar')
        op = input_values()
        #clean_terminal()
        
        #todo: consertar 1, 2, priorization_print, 5, 4 - -revisar tudo

        if op == 1:
            print()
            print(*squad.keys(),sep=', ')
            print('Que consagrado irá perder pontos?')
            people = input().strip().capitalize()

            while people not in squad.keys():
                print(squad.keys())
                print('Que consagrado irá perder pontos?')
                people = input().strip().capitalize()

            print(f'Quantos pontos serão tirados do(a) {people}? atualmente tem {squad[people]}.')
            squad[people]['points'] -= input_values()
            if counter(squad) < general_points:
                squad, general_points = prioritization(squad, general_points)

        elif op == 2:
            generate_csv(squad)
            sleep(1)
            print('Fim da priorização da sprint.')
            sleep(1)
            return
        elif op == 3:
            print('bye')
            return
        elif op == 4:
            print('Espere por 3 segundos, voltará ao menu anterior.')
            priorization_print(squad)
            sleep(3)
        elif op == 5:
            print('Dados foram apagados...')
            squad = initial_fase
            squad, general_points = prioritization(squad, general_points)
        elif op == 9:
            vult()
            return
        else:
            print("Por favor escolha uma das opções listadas!")

#priorization_order()

if __name__ == '__main__':
    main()

#pyautogui.hotkey('ctrl','j')
