from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from base import Page
from locators import *
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import pandas as pd
from pathlib import Path
import io

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


###############
###############

class MainPage(Page):
    def __init__(self, driver):
        self.locator = MainPageLocatars
        super().__init__(driver)  # Python3 version

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.PhonesTV) else False

    def click_PhonesTV(self):
        self.hover(*self.locator.PhonesTV)
        self.find_element(*self.locator.PhonesTV).click()
        return PhonesTVPage(self.driver)

    def AddResultsInExcel(self):
        df = pd.read_csv('Case1_Results.txt',encoding="utf-8", engine='python')
        df.to_excel('excel.xlsx', 'Sheet1')


    def AddResultsInDB(self,list_data):
        conn = MySQLdb.connect(host="localhost",
                               user="test",
                               passwd="1111",
                               db="test")
        x = conn.cursor()
        try:
            x.execute("""INSERT INTO list(record) VALUES (%s)""", (str(list_data)))
            conn.commit()
        except:
            conn.rollback()

        conn.close()

###############
###############

class PhonesTVPage(Page):
    def __init__(self, driver):
        self.locator = PhonesTVLocatars
        super(PhonesTVPage, self).__init__(driver)  # Python2 version

    def click_Phones(self):
        self.hover(*self.locator.Phones)
        self.find_element(*self.locator.Phones).click()
        return PhonesPage(self.driver)

###############
###############

class PhonesPage(Page):
    def __init__(self, driver):
        self.locator = SmartsLocatars
        super(PhonesPage, self).__init__(driver)  # Python2 version

    def click_Smarts(self):
        self.hover(*self.locator.Smarts)
        self.find_element(*self.locator.Smarts).click()
        return SmartsListPage(self.driver)


###############
###############

class SmartsListPage(Page):

    def __init__(self, driver):
        self.locator = SmartsListLocatars
        super(SmartsListPage, self).__init__(driver)  # Python2 version

    def write_Results(self,rdata):
        with io.open('Case1_Results.txt', 'wb') as the_file:
            the_file.write(rdata)

    def click_Second(self):
       # self.hover(*self.locator.secondPage)
        self.find_element(*self.locator.secondPage).click()
        try:
            WebDriverWait(self, 10).until(EC.presence_of_element_located((By.XPATH, self.locator.secondPage_Check)))
        finally:
            WebDriverWait(self, 10)
        return SmartsListPage(self.driver)

    def click_Third(self):
        #self.hover(*self.locator.thirdPage)
        self.find_element(*self.locator.thirdPage).click()
        try:
            WebDriverWait(self, 10).until(EC.presence_of_element_located((By.XPATH, self.locator.thirdPage_Check)))
        finally:
            WebDriverWait(self, 10)
        return SmartsListPage(self.driver)

    def get_List(self):
        return self.get_data_list(self.locator.AllItems)

