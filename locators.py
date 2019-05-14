from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name

class MainPageLocatars(object):
  PhonesTV = (By.LINK_TEXT,"Смартфоны, ТВ и электроника")

class PhonesTVLocatars(object):
  Phones = (By.PARTIAL_LINK_TEXT, "Телефоны")

class SmartsLocatars(object):
  Smarts = (By.XPATH, '//a[contains(@href, "/filter/preset=smartfon/")]')

class SmartsListLocatars(object):
  AllItems = '//a[contains(@onclick, "document.fireEvent(\'goodsTitleClick\'")]'
  secondPage = (By.XPATH, '//a[contains(@href, "page=2")]')
  secondPage_Check ="//li[@id='page2'][contains(@class, 'active')]"
  thirdPage =  (By.XPATH,'//a[contains(@href, "page=3")]')
  thirdPage_Check = "//li[@id='page3'][contains(@class, 'active')]"
