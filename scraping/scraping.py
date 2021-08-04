# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager


class Scraping:
    driver = None
    actions = None

    def __init__(self, url, profile, options, log, load_time=40):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager(
        ).install(), firefox_profile=profile, options=options)
        self.actions = ActionChains(self.driver)
        self.driver.get(url)
        log(1, 'Fazendo Requisição ao Site...')
        time.sleep(load_time)

    def click(self, xpath, timer=2):
        self.driver.find_element_by_xpath(xpath).click()
        time.sleep(timer)

    def move_and_click(self, xpath, timer=1):
        context = self.driver.find_element_by_xpath(xpath)
        self.actions.move_to_element(context)
        self.actions.click()
        self.actions.perform()
        time.sleep(timer)

    def click_one(self, xpath, index=0, timer=4):
        elements = self.driver.find_elements_by_xpath(xpath)
        elements[index].click()
        time.sleep(timer)

    def input_key(self, xpath, index, keys, timer=5):
        input_text = self.driver.find_elements_by_xpath(xpath)
        input_text[index].clear()
        for key in keys:
            input_text[index].send_keys(key)

        time.sleep(3)
        input_text[index].send_keys(Keys.ENTER)
        time.sleep(timer)

    def input_keys_top(self, xpath, keys, timer=5):
        ''''
        Seleciona o input que estiver mais ao topo do ```xpath``` buscado,\n
        ou seja, o último elemento da lista
        \tEx:\n
        ```
            xpath = "//*[contains(text(), "EX")]"
            res = [<selenium element 1>, <selenium element 2>, <selenium element 3>]
            seleted index = len(res) - 1
        ``` 
        '''
        input_text = self.driver.find_elements_by_xpath(xpath)
        last_index = len(input_text) - 1
        input_text[last_index].clear()
        for key in keys:
            input_text[last_index].send_keys(key)

        time.sleep(3)
        input_text[last_index].send_keys(Keys.ENTER)
        time.sleep(timer)

    def scroll(self, element):
        self.driver.execute_script(
            "document.querySelector('{}').scrollIntoView()".format(element))

    def execute_script(self, script):
        self.driver.execute_script(script)

    def close(self):
        self.driver.quit()
