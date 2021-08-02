import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from scraping.log import gen_log
from os import listdir, path
from os.path import isfile, join
from scraping.convert import gen_csv, to_csv


def execute():
    url = 'https://qsprod.saude.gov.br/extensions/DEMAS_C19Vacina/DEMAS_C19Vacina.html'

    dir_download = join(path.dirname(path.realpath(__file__)), 'downloads')

    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir",
                           dir_download)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                           "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    options = Options()
    options.add_argument('--headless')

    try:
        # Auto configuração de GeckoDriver
        driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install(), firefox_profile=profile, options=options)
        print(' ---- Iníciando Script ---- ')
        print(' ---- Carregando... ---- ')
        driver.get(url)
        time.sleep(40)
        element = "//table[@class='ng-scope']//td"

        driver.execute_script(
            "document.querySelector('table').scrollIntoView()")

        # Click em Download
        driver.find_element_by_xpath(
            "//*[contains(text(), 'Baixar Dados por Município')]").click()

        time.sleep(10)
        gen_log('Success', 'Download efetuado com sucesso!')

        print(' ---- Fim do Script ---- ')
        driver.quit()
    except:
        print(' ---- Erro. O site está congestionado ---- ')
        gen_log('Error', 'Não foi possível efetuar o download.')

    files = [f for f in listdir(dir_download) if isfile(
        join(dir_download, f))]

    try:
        to_csv(files[0])
        gen_log('Success', 'Arquivo convertido com sucesso!')
    except:
        gen_log('Error', 'Não foi possível converter o arquivo.')

    try:
        gen_csv('PI')
        gen_log('Success', 'Filtro de Estado executado com sucesso!')
    except:
        gen_log('Error', 'Não foi possível filtrar o arquivo')
