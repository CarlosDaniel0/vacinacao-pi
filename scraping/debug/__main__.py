from scraping import Scraping
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from os.path import join, dirname ,realpath, isfile
from os import listdir
from convert import Convert
from logger import Logger
from util import Util
import logger

base_dir = dirname(realpath(__file__))
dir_download = join(base_dir, 'downloads')

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir",
                        dir_download)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")


options = Options()
# options.add_argument('--headless')

#
#    PRIMEIRA ETAPA
#
try:
    # Instancia a Classe e abre webdriver
    scraping = Scraping('https://qsprod.saude.gov.br/extensions/DEMAS_C19Vacina/DEMAS_C19Vacina.html', profile,options, Logger.show)

    Logger.show(1, 'Click no menu lateral')
    # Clique no Menu
    scraping.click("//paper-icon-button[@class='filter-drawer-toggle x-scope paper-icon-button-0']")

    Logger.show(1, 'Clique em UF')
    # Clica em UF em uma lista de Elementos
    scraping.click_one("//div[@class='qv-filterpane-column ng-scope']//div[@class='ng-scope qv-filterpane-collapsed']")

    Logger.show(1, 'Digitando "PI " na busca')
    # Clica no input de busca e envia os dados "PI " e aperta enter

    scraping.input_keys_top("//input[@placeholder='Pesquisar na caixa de listagem']", ['PI '])
    # scraping.input_keys_top("//input[@placeholder='Pesquisar na caixa de listagem']", ['PI '])

    Logger.show(1, 'Clique na div de context para fechar o menu')
    # Clica na div de contexto para fechar o menu
    scraping.move_and_click("//div[@id='scrim']")
    logger.Logger.show
    Logger.show(1, 'Scroll para o painel')
    # Desce para encontrar o elemento
    scraping.scroll("#QV1-G11A")

    Logger.show(1, 'Clique no botão de download')
    # Clica no botão de download
    scraping.click("//div[@id='QV1-G11A-menu']", timer=5)

    Logger.show(2, 'Script executado com sucesso!')
    scraping.close()

    print('')
#
#    SEGUNDA ETAPA
#
    try:
        Logger.show(1, 'Buscando arquivo')
        # Converter o arquivo XLSX para CSV
        files = [f for f in listdir(dir_download) if isfile(join(dir_download, f))]
        convert = Convert(
            dir_download, 
            join(Util.change_dir(base_dir,down_levels=1), 'app', 'rnds'),
            files[0],
            'vacinacao_pi_rnds.csv')

        Logger.show(1, 'Convertendo arquivo para CSV...')
        convert.to_csv()
        Logger.show(2, 'Conversão efetuada com sucesso!')

    except:
        Logger.show(0, 'Falha ao converter o arquivo para CSV')
except:
    Logger.show(0, 'Falha ao executar o script, verifique o site de destino!')


print('')
