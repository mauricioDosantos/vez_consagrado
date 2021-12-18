# -*- coding: utf-8 -*-
# author: Mauricio
import requests as rqt
from requests.auth import HTTPBasicAuth
from datetime import datetime
from dateutils import relativedelta
import json
import time
import pprintpp
from operator import itemgetter



def generate_csv(data):
    print('Gerando csv....')
    sleep(1)
    with open('priorização.csv','w+',encoding='utf-8') as file:
        file.write('Priorizador|Pontos\n')
        for key,value in data.items():
            val_ = value['points']
            file.write(f'{key}|{val_}\n')
    
    print('Arquivo salvo no mesmo diretório do arquivo')


def get_data_jira():
    """
    Data structure:
        {cs:{points:,state:,}}
    """

    __dict = {}

    date = str(datetime.now().date() - relativedelta(days=7))

    keys = {
        'JIRA_USER': 'paulo.souza@sensedata.com.br',
        'JIRA_PW': 'xAgPeVji4UURafRlU1fb97B0'
        }
    start_at = 0
    while True:

        # project = SA AND issuetype in (Retrabalho, Task) AND status in ("Erro QA", "In Progress", "Pronto para QA", QA, "QA Cliente") AND resolution = Unresolved ORDER BY updated DESC, created ASC
        url = ('https://sensedata.atlassian.net/rest/api/3/search?jql=project="SA" AND issuetype IN ("Retrabalho", "Task") AND status IN ("Erro QA", "In Progress", "Pronto para QA", "Disponivel para QA" , "QA Cliente") AND resolution = "Unresolved" ORDER BY summary ASC, created DESC&startAt={}').format(start_at)
        ##tirei o QA
        #url = 'https://sensedata.atlassian.net/rest/api/3/search?jql=project="SA" AND status IN ("Erro QA","Pronto para QA","QA","QA Cliente","In Progress") AND resolution = "Unresolved" ORDER BY created DESC'

        #project = "SA" AND status IN ("Erro QA","Pronto para QA","QA","QA Cliente","In Progress") AND resolution = "Unresolved" ORDER BY created DESC

        payload = rqt.get(
            url,
            auth=HTTPBasicAuth(keys['JIRA_USER'], keys['JIRA_PW'])
        )
        if payload.status_code == 404:
            break
        data = payload.json()

        start_at += data.get('maxResults')

        print(payload.status_code)
        print(data.get('maxResults'))
        print(data.get('total'))
        issues = data.get('issues')
        pprintpp.pprint(issues)
        if not issues:
            break
        
        _cx = ['Gabriel Lima', 'Raquel Pontes Martins', 'Ana Paula Petrasso']
        _cs = ['Erimar Amorim', 'Jucélio Fernandes', 'Ana Carolina Souza']
        _is = ['Maria Amália Barros', 'Ramon Gouvea']
        _cx_customer = {
            'Ana Paula Petrasso': ['c53 Take', 'c56 Total voice c76 Ramper, c103 c151 c141  c77 c32 c32_1 c92(costa brava) c174(telluria) c148(saude id) c172(siteware) c171(infoprice) mega c132(construtordevendas) c152(clubpetro) c131(inchurch) c127(auto avaliar) c121(code7) c116(manager saúde) c33(digitro)'],
            'Gabriel Lima': ['c13 vindi c169(vipred) c167(iclinic) c166(prevision) c150(virtus pay) c142(vee beneficios) c139(hilab) c130(hbsis) c95(phonetrak) c87(vr software) c85 c71(iev) c68(checklistfacil) c58(aegro) c45(sanhkya) c22(geekie) c15(mercafacil) '],
            'Raquel Pontes Martins': ['c65(senior) c63(boa vista) c138(clin) c113FindUP(sem num) c114(matera) c20(hivecloud) c43(somos educação) c44(fortes) c115(logicalis)']}
        
        __dict.update(
            {value.lower().strip(): {'points': 0, 'state': True} for value in _cs}
            )
        #saber o ponto de acordo com o cs ou is do cliente

        '''fields.assignee - cara que está fazendo
        fields.created - criação
        fields.creator - criador
        fields.reporter - esse que deve ser pego - displayName
        # tudo dentro do fields
        status.name - tipo do status - erro QA
        status.statusCategory.name - lane - In progress
        summary - titulo do card - '[QC] 10/09'
        updated - ultima att - data e hora
        key - numero do card - esse fora do fields
        project.name - 'Squad Axé'
        subtask - False or True
        customfield_10010 - []- nome da sprint está aqui dentro - customfield_10010.state -> Ex: future | customfield_10010.name -> Sprint 50 axé
        customfield_10049 - Points
        issuetype.name - Task - Retrabalho
        customfield_10008- SA-1265 -card do epiclink - pega o tenant
        como SA-1265 essa é a key do epic é só pesquisar por ela pegar o título separa no - de/para que de quem'''
        '''{
                'boardId': 65,
                'endDate': '2021-09-17T20:00:00.000Z',
                'goal': '',
                'id': 575,
                'name': 'Sprint 49 axé',
                'startDate': '2021-09-06T13:58:23.389Z',
                'state': 'active',
            }'''


        for issue in issues:

            #pprintpp.pprint(issue)
            fields = issue.get('fields')
            reporter = (
                fields.get('reporter').get('displayName')
                ).lower().strip()
            point = fields.get('customfield_10049') or 0
            if reporter in __dict:
                __dict[reporter]['points'] += point
                continue

            __dict[reporter] = {'points': point, 'state': True}

    return __dict
'''
dict_keys(['statuscategorychangedate', 'issuetype', 'timespent', 'project', 'fixVersions', 'aggregatetimespent', 'resolution', 'resolutiondate', 'workratio', 'lastViewed', 'watches', 'customfield_10060', 'customfield_10061', 'created', 'priority', 'labels', 'timeestimate', 'aggregatetimeoriginalestimate', 'versions', 'issuelinks', 'assignee', 'updated', 'status', 'components', 'customfield_10050', 'timeoriginalestimate', 'customfield_10051', 'customfield_10052', 'customfield_10053', 
'description', 'customfield_10054', 'customfield_10010', 'customfield_10011', 'customfield_10055', 'customfield_10056', 'customfield_10012', 'customfield_10057', 'customfield_10013', 'customfield_10058', 'customfield_10049', 'security', 'customfield_10008', 'aggregatetimeestimate', 'customfield_10009', 'summary', 'creator', 'subtasks', 'reporter', 'aggregateprogress', 'customfield_10000', 'customfield_10001', 'customfield_10004', 'environment', 'duedate', 'progress', 'votes'])  
'''

    #return

def initializer():

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
    print('Caio Ribeiro, Ramon Gouvea, Ana Paula, Jucélio Fernandes (enter pega padrão)')
    print('1- Criar própria lista')
    op = input().strip()
    
    if op == '':
        peoples = ['Caio Ribeiro','Jucélio Fernandes', 'Ramon Gouvea', 'Ana Paula']
    elif op == '1':
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
    return


def input_values(type_='f'):
    """
    type_ = s strings
    type_ = f integer
    """
    if type_ == 'f':
        value = ''
        while type(value) != float:
            try:
                value = float(input())
            except ValueError:
                print('Que valor é esse? Oxente. Digite certo homi(muié).')
        return value


def choices(i, _tuple, sprint_points) -> tuple:
    _tuple[1]['order'] = i

    print('Pular priorização -1(Vai para o próximo)  ||  Deixar de priorizar -2 (Esse jogador) || Alterar pontos da sprint -3 || Fechar gerando csv -4')
    print(f'Vez do(a) consagrado(a) {_tuple[0]}. Quantos pontos irá subir nessa rodada?')
    value = input_values()

    if value == -1:
        return sprint_points, _tuple

    elif value == -2:
        _tuple[1]['state'] = False
        return sprint_points, _tuple

    elif value == -3:

        print(f'Quantidade de pontos definida é {sprint_points}')
        print('Qual a nova quantidade de pontos?')
        sprint_points = input_values()
    
    elif value == -4:

        generate_csv(_tuple)
        _tuple = None
        return sprint_points, _tuple

    else:
        _tuple[1]['points'] += value

    return sprint_points, _tuple


# aqui ficará chamda das funções
def main():
    """
    Data structure:
        {cs:{points:,state:,}}
    """
    __dict = get_data_jira()
    #pprintpp.pprint(__dict)
    order = sorted(__dict.items(), key=lambda t: t[1]['points'])
    pprintpp.pprint(order)

    print('Quantidades de pontos da Sprint Axé')
    sprint_points = input_values()
    points_played = 0
    while True:
    # play rule
        if points_played >= sprint_points:
            break
        for i, _tuple in enumerate(order):
            sprint_points, _tuple = choices(i, _tuple, sprint_points)

            if _tuple == None:
                break
            print(_tuple)
            __dict.update({_tuple[0]: _tuple[1]})

        if _tuple == None:
            break

        order = sorted(__dict.items(), key=lambda t: itemgetter(t[1]['points'], t[1]['order']))

    # structure
    #players = {<name>: {points: , enabled: , round: }}

    return


if __name__ == '__main__':
    main()
