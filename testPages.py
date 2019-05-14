import unittest
from selenium import webdriver
from pages import *
from testCases import test_cases
from locators import *
from selenium.webdriver.common.by import By


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestPages(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.get("https://rozetka.com.ua/")

    def test_Case1(self):
        print("\n" + str(test_cases(0)))
        page = MainPage(self.driver)
        PhonesTV_P = page.click_PhonesTV()
        Phone_P=PhonesTV_P.click_Phones()
        Smarts_P=Phone_P.click_Smarts()
        list_from_page1=Smarts_P.get_List()
        Smarts_P2 = Smarts_P.click_Second()
        list_from_page2 = Smarts_P2.get_List()
        Smarts_P3 = Smarts_P2.click_Third()
        list_from_page3 = Smarts_P3.get_List()
        datar=datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'=====PAGE1======'+'\n'+list_from_page1+'=====PAGE2======'+'\n'+list_from_page2+'=====PAGE3======'+'\n'+list_from_page3
        datar=datar.encode(encoding='UTF-8', errors='strict')
        #page.SendResultsViaEmail(datar)   Как и куда слать в задании не ясно! Это может быть sendmail\Jenkins или доп email библиотеки
        Smarts_P3.write_Results(datar)
        page.AddResultsInDB(datar)  #pymysql
        page.AddResultsInExcel() #pandas
        self.assertIn("preset=smartfon", Smarts_P.get_url())


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)

