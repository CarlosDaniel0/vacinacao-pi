import csv
from flask import json


def to_json(file):
    res = []
    vacinas = []
    with open(file, 'r') as reader:
        data = csv.reader(reader)
        c = 0

        for line in data:
            if c != 0:
                data = {}
                data['municipio'] = line[0]
                data['cod'] = line[1]
                data['uf'] = line[2]
                data['regiao'] = line[3]
                item_vacina = {
                    'fabricante': line[4],
                    'doses_aplicadas': line[5],
                    'dose_1': line[6],
                    'dose_2': line[7]
                }
                data['vacinas'] = []
                vacinas.append(item_vacina)
                res.append(data)
            c += 1

    n = 4
    vacinas_agrupagas = [vacinas[i:i + n] for i in range(0, len(vacinas), n)]

    new_res = []
    indexes = []
    for i in range(len(res) - 1):
        if res[i] != res[i + 1]:
            new_res.append(res[i])
            indexes.append(i)

    print(indexes)
    for i in range(len(new_res)-1):
        new_res[i]['vacinas'] = vacinas_agrupagas[i]

    return new_res

# {
#   [
#     {
#       municipio: 'Monsenhor Gil',
#       cod: '0500df5d0',
#       uf: 'PI',
#       fabricante: {
#         'fio cruz' : {
#           'doses_aplicadas': '',
#           '1 dose': '',
#           '2 dose': ''
#         },
#         'butantan': {
#           'doses_aplicadas': '',
#           '1 dose': '',
#           '2 dose': ''
#         },
#         'pfizer': {
#           'doses_aplicadas': '',
#           '1 dose': '',
#           '2 dose': ''
#         },
#         'janssen':  {
#           'doses_aplicadas': '',
#           '1 dose': '',
#           '2 dose': ''
#         },
#       }
#     }
#   ]

# }
