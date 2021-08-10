from os import path
from os.path import join

class Util:
    @staticmethod
    def change_dir(base_dir, down_levels=0, up_to=''):
        ''' 
        Defina para qual diretório deseja avançar ou retroceder\n
        \down levels:  Quantidade de pastas para descer\n
        \t\t```down levels = 3``` Desce 3 diretórios\n
        \tup to: pasta de destino * opcional\n
        \t\t```up to = 'logs' \t {base dir}/logs``` \n
        \t\t```up to = 'app/logs' \t {base dir}/app/logs}```
        '''

        list_dir = base_dir.split('/')
        if up_to:
            return path.join(base_dir, up_to)
        elif down_levels:
            for i in range(down_levels):
                list_dir.pop()
            return '/'.join(list_dir)

    @staticmethod
    def scape_string(string, space=False):
        '''
        Retorna uma string sem caracteres especiais
        ```string a = 'João foi na casa de Antônio para tocar violão'```
        \t{@return} 'Joao_foi_na_casa_de_Antonio_para_tocar_violao'
        '''
        string_aux = string
        old = 'Á É Í Ó Ú á é í ó ú À à Ç ç Â Ê Ô â ê ô Ã Õ ã õ'.split(' ')
        replacement = 'A E I O I a e i o u A a C c A E O a e o A O a o'.split(' ')
        if not space:
            old.append(' ')
            replacement.append('_')

        for i in range(len(old)):
            string_aux = string_aux.replace(old[i], replacement[i])
        return string_aux