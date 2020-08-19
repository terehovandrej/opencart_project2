from time import sleep

import allure
from selenium.webdriver.common.by import By
from .basepage import BasePage


class ProductsPage(BasePage):
    add_button = (By.XPATH, '//a[@data-original-title="Add New"]')
    main_table = (By.XPATH, '//table')
    image_tab = (By.XPATH, '//a[text() = "Image"]')
    data_tab = (By.XPATH, '//a[text() = "Data"]')
    product_image_icon = (By.XPATH, '//a[@id="thumb-image"]')
    edit_image_button = (By.XPATH, '//button[@id="button-image"]')
    image_icon = (By.XPATH, '//img[@title="iphone.jpg"]')
    submit_button = (By.XPATH, '//button[@type="submit"]')
    product_name_input = (By.XPATH, '//input[@id="input-name1"]')
    meta_tag_title_input = (By.XPATH, '//input[@id="input-meta-title1"]')
    model_input = (By.XPATH, '//input[@id="input-model"]')
    success_alert = (By.XPATH, '//div[contains(text(), "Success: You have modified products!")]')
    delete_button = (By.XPATH, '//button[@data-original-title="Delete"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def _set_product_name_(self, name):
        self.find_element(locator=self.product_name_input).clear()
        self.find_element(locator=self.product_name_input).send_keys(name)

    def _set_meta_tag_tittle_(self, name):
        self.find_element(locator=self.meta_tag_title_input).clear()
        self.find_element(locator=self.meta_tag_title_input).send_keys(name)

    def _set_model_input_(self, name):
        self.find_element(locator=self.model_input).clear()
        self.find_element(locator=self.model_input).send_keys(name)

    @allure.step
    def click_add_product_button(self):
        self.find_element(locator=self.add_button).click()

    def click_submit_button(self):
        self.find_element(locator=self.submit_button).click()

    @allure.step
    def click_edit_button(self, product):
        with allure.step("Нажимаю на кнопку редактировать"):
            edit_button = f'//table//tr/td[text()="{product}"]/../td/a'
            self.find_element_by_xpath(selector=edit_button).click()

    @allure.step
    def open_image_tab(self):
        self.find_element(locator=self.image_tab).click()

    @allure.step
    def open_data_tab(self):
        self.find_element(locator=self.data_tab).click()

    def set_new_product_required_fields(self, product, meta_tag, model):
        with allure.step("Заполняю обязательные поля при добавлении нового продукта"):
            self._set_product_name_(product)
            self._set_meta_tag_tittle_(meta_tag)
            self.open_data_tab()
            self._set_model_input_(model)

    @property
    def main_table_element(self):
        return self.find_element(self.main_table)

    @property
    def success_alert_element(self):
        return self.find_element(self.success_alert)

    @allure.step
    def check_product_in_table(self, product):
        with allure.step(f"Проверяю наличие продукта {product} в таблице"):
            product = f'//table//tr/td[text()="{product}"]'
            assert self.find_element_by_xpath(selector=product, time=10)

    def check_product_is_not_in_table(self, product):
        with allure.step(f"Проверяю отсутствие продукта {product} в таблице"):
            product = (By.XPATH, f'//table//tr/td[text()="{product}"]')
            assert self.test_element_does_not_present(product)

    @allure.step
    def delete_product_from_table(self, product):
        product_checkbox = f'//table//tr/td[text()="{product}"]/../td/input'
        self.find_element_by_xpath(selector=product_checkbox, time=10).click()
        self.find_element(self.delete_button).click()
        self.accept_alert()



