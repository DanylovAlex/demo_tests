from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def open_product_page(self):
        self.driver.get()

    def check_page(self, txt):
        xp_bottom = '//*[@id="page-title-heading"]'
        element = self.driver.find_element(By.XPATH, xp_bottom)
        assert element.text == txt # 'Men'
