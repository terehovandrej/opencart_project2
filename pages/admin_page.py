from time import sleep

from selenium.webdriver.common.by import By
from .basepage import BasePage


class AdminPage(BasePage):
    username = (By.ID, 'input-username')
    password = (By.ID, 'input-password')
    submit_button = (By.CSS_SELECTOR, 'button')
    user_profile_icon = (By.XPATH, '//a[text() = "John Doe "]')
    logout_button = (By.XPATH, '//span[text()="Logout"]')
    navigation_catalog = (By.XPATH, '//a[text()=" Catalog"]')
    navigation_products = (By.XPATH, '//a[text()="Products"]')
    navigation_filters = (By.XPATH, '//a[text()="Filters"]')
    navigation_categories = (By.XPATH, '//a[text()="Categories"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def logout(self):
        self.find_element(locator=self.logout_button).click()

    def go_to_products(self):
        self.find_element(locator=self.navigation_catalog).click()
        self.find_element(locator=self.navigation_products).click()

    def go_to_categories(self):
        self.find_element(locator=self.navigation_catalog).click()
        self.find_element(locator=self.navigation_categories).click()

    def go_to_filtres(self):
        self.find_element(locator=self.navigation_catalog).click()
        self.find_element(locator=self.navigation_filters).click()

    @property
    def user_profile_element(self):
        product = (By.XPATH, '//table//tr/td[text()="iphone"]')
        return product

