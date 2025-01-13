from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.home_link = 'https://magento.softwaretestingboard.com/'

    def open(self):
        self.driver.get(self.home_link)

    def click_page(self, xpath):
        menu = self.driver.find_element(By.XPATH, xpath)
        menu.click()
