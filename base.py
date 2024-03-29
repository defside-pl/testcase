from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# this Base class is serving basic attributes for every single page inherited from Page class

class Page(object):
    def __init__(self, driver, base_url='https://rozetka.com.ua/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 10
 
    def find_element(self, *locator):
        return self.driver.find_element(*locator)
 
    def open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        
    def get_title(self):
        return self.driver.title
        
    def get_url(self):
        return self.driver.current_url
    
    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def get_data_list(self, locator):
        ielements = self.driver.find_elements(By.XPATH,locator)
        res=''
        ielements
        for elem in ielements:
            res=res+elem.text+'\n'
        return res
