from datetime import datetime
from os import path

dir = path.dirname(path.realpath(__file__))


def gen_log(status, message):
    date = datetime.now()

    message = '{} : STATUS: {} : MESSAGE: {}\n'.format(
        date.strftime('%d/%m/%Y - %H:%M'), status, message)
    with open(path.join(dir, 'logs', 'log.txt'), 'a+') as reader:
        reader.write(message)
        reader.close()
