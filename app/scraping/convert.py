import pandas as pd
from os import remove, path
import csv

dir = path.dirname(path.realpath(__file__))


def public_dir(file):
    new_dir = dir.split(
        '/')
    new_dir.pop()
    return path.join('/'.join(new_dir), 'public', file)


def to_csv(name):
    data_xls = pd.read_excel(
        path.join(dir, 'downloads', name), 'Sheet1', dtype=str, index_col=None)
    data_xls.to_csv(public_dir('data.csv'), encoding='utf-8', index=False)

    print(' ---- Arquivo CSV Gerado com sucesso! ---- ')

    remove(path.join(dir, 'downloads', name))
    print(' ---- Arquivo XLSX Removido com sucesso! ---- ')


def gen_csv(dir):

    new_file = []
    c = 0
    with open(public_dir('data.csv'), 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[2] == 'PI':
                line = ','.join(row)
                new_file.append(line)  # Body
            elif c == 0:
                line = ','.join(row)
                new_file.append(line)  # Header
            c += 1
        csv_file.close()

    with open(public_dir('data.csv'), 'w') as csv_file:
        for i in new_file:
            csv_file.write(i + '\n')  # Reescrita de arquivo
        csv_file.close()

    print(' ---- Filtro executado com sucesso! ---- ')
