from datetime import datetime
from os import path
from bcolors import bcolors

dir = path.dirname(path.realpath(__file__))

class Logger:
    @staticmethod
    def show(status, message):
        '''
        Status\n
        ```
        status = 0 FAIL
        status = 1 INFORMATION
        status = 2 SUCCESS
        ```
        '''

        date = datetime.now()
        with open(path.join(dir, 'logs', 'log.txt'), 'a+') as reader:
                formated_date = date.strftime('%d/%m/%Y - %H:%M:%S')
                if status == 0:
                    status = 'FAIL'
                    print('{}:'.format(
                        bcolors.bold(formated_date)),
                        bcolors.fail(message))
                    
                elif status == 1:
                    status = 'INFO'
                    print('{}:'.format(
                        bcolors.bold(formated_date)), 
                        bcolors.info(message))
                elif status == 2:
                    status = 'SUCCESS'
                    print('{}:'.format(
                        bcolors.bold(formated_date)), 
                        bcolors.ok(message))
                message = '{} : STATUS: {} : MESSAGE: {}\n'.format(
                    formated_date, status, message)
                reader.write(message)
                reader.close()

    @staticmethod
    def loading():
        pass

