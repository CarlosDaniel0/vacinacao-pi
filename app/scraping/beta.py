import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

url = 'https://qsprod.saude.gov.br/extensions/DEMAS_C19Vacina/DEMAS_C19Vacina.html'

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir",
                       '/home/daniel/Documentos/python/dados-vacinacao-ms/')
profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                       "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

options = Options()
options.headless = True
# Auto configuração de GeckoDriver
driver = webdriver.Firefox(
    executable_path=GeckoDriverManager().install(), firefox_profile=profile)

driver.get(url)
time.sleep(120)
print('chegou aqui!')

element = "//table[@class='ng-scope']//td"

try:
    driver.execute_script("document.querySelector('table').scrollIntoView()")
except:
    time.sleep(10)
    driver.execute_script("document.querySelector('table').scrollIntoView()")
c = 1
for e in WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, element))):
    # print(e.text, "index: ", c)
    if c == 7:
        e.click()  # Click no + de Nordeste
        time.sleep(2)

    if c == 14:
        e.click()  # Click no + de AL
        time.sleep(5)
        break
    c += 1

c = 1
results = driver.find_elements_by_xpath("//table[@class='ng-scope']//td")
for result in results:
    # print(result.text, "index: ", c)
    if c == 56:
        result.click()  # Click no + do PI
        time.sleep(3)
        break
    c += 1

element = driver.find_element_by_xpath(
    "//table[@class='ng-scope']")
html_content = element.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')
# results = driver.find_elements_by_xpath("//table[@class='ng-scope']//tr//td")


print(soup)
# c = 1
# for result in results:
#     print(result.text, "-- \tindex: ", c)
#     c += 1

# time.sleep(5)  # Tempo para requisição de PI

# # driver.execute_script(
# #     "document.querySelector('.lui-icon--tick').scrollIntoView()")

# # driver.find_element_by_xpath(
# #     "//*[@class='sel-toolbar-span-icon lui-icon ng-binding lui-icon--tick']").click()

# time.sleep(1000)

# driver.find_element_by_xpath(
#     "//*[contains(text(), 'Baixar Dados por Município')]").click()

# time.sleep(10)
# print('acabou!')

# driver.quit()
