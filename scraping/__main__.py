from scraping import Scraping
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from os.path import join, dirname, realpath, isfile
from os import listdir
from convert import Convert
from logger import Logger
from util import Util
import logger
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
options.add_argument('--headless')

#
#    PRIMEIRA ETAPA
#
try:
    scraping = Scraping('https://qsprod.saude.gov.br/extensions/DEMAS_C19Vacina/DEMAS_C19Vacina.html',
                        profile, options, Logger.show, load_time=50)

    Logger.show(1, 'Desceu para a tabela')
    scraping.scroll('table')

    Logger.show(1, 'Clicou no + de nordeste')
    element = "//table[@class='ng-scope']//td"
    scraping.click_one(element, 6)

    Logger.show(1, 'Clicou no - de AL')
    scraping.click_one(element, 13, timer=5)

    Logger.show(1, 'Clicou no PI')
    scraping.click_one(element, 56)

    Logger.show(1, 'Sobe para a parte doses distribuidas')
    scraping.scroll('#QV1-G11A')

    Logger.show(1, 'Clicou no botão de download')
    scraping.click("//div[@id='QV1-G11A-menu']", timer=10)

    Logger.show(2, 'Download efetuado com sucesso!')
    scraping.close()
#
#    SEGUNDA ETAPA
#
    try:
        Logger.show(1, 'Buscando arquivo')
        # Converter o arquivo XLSX para CSV
        files = [f for f in listdir(dir_download)
                 if isfile(join(dir_download, f))]
        convert = Convert(
            dir_download,
            join(Util.change_dir(base_dir, down_levels=1), 'app', 'rnds'),
            files[0],
            'vacinacao_pi_rnds.csv')

        Logger.show(1, 'Convertendo arquivo para CSV...')
        convert.to_csv()
        Logger.show(2, 'Conversão efetuada com sucesso!')
        
        with open(join(Util.change_dir(base_dir, down_levels=1), 'app', 'rnds', 'vacinacao_pi_rnds.csv'), 'r') as file:
            csv_file = csv.reader(file)
            for i in csv_file:
                print(i)
    except:
        Logger.show(0, 'Falha ao converter o arquivo para CSV')
except:
    Logger.show(0, 'Falha ao executar o script, verifique o site de destino!')
