from selenium.webdriver.common.by import By
from .basepage import BasePage


class CategoriesPage(BasePage):
    add_category_button = (By.XPATH, '//a[@data-original-title="Add New"]')
    submit_button = (By.XPATH, '//button[@type="submit"]')
    category_name_input = (By.XPATH, '//input[@id="input-name1"]')
    meta_tag_title_input = (By.XPATH, '//input[@id="input-meta-title1"]')
    success_alert = (By.XPATH, '//div[contains(text(), "Success: You have modified categories!")]')
    delete_button = (By.XPATH, '//button[@data-original-title="Delete"]')
    rebuild_button = (By.XPATH, '//a[@data-original-title="Rebuild"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def _set_category_name_(self, name):
        self.find_element(locator=self.category_name_input).clear()
        self.find_element(locator=self.category_name_input).send_keys(name)

    def _set_meta_tag_tittle_(self, name):
        self.find_element(locator=self.meta_tag_title_input).clear()
        self.find_element(locator=self.meta_tag_title_input).send_keys(name)

    def click_add_category_button(self):
        self.find_element(locator=self.add_category_button).click()

    def click_submit_button(self):
        self.find_element(locator=self.submit_button).click()

    def click_edit_button(self, category):
        edit_button = f'//table//tr/td[text()="{category}"]/../td/a'
        self.find_element_by_xpath(selector=edit_button).click()

    def set_category_required_fields(self, category, meta_tag):
        self._set_category_name_(category)
        self._set_meta_tag_tittle_(meta_tag)

    @property
    def success_alert_element(self):
        return self.find_element(self.success_alert)

    def check_category_in_table(self, category):
        product = f'//table//tr/td[text()="{category}"]'
        assert self.find_element_by_xpath(selector=product, time=10)

    def check_category_is_not_in_table(self, category):
        product = (By.XPATH, f'//table//tr/td[text()="{category}"]')
        assert self.test_element_does_not_present(product)

    def delete_category_from_table(self, category):
        category_checkbox = f'//table//tr/td[text()="{category}"]/../td/input'
        self.find_element_by_xpath(selector=category_checkbox, time=10).click()
        self.find_element(self.delete_button).click()

    def accept_delete_category_alert(self):
        self.accept_alert()

    def dismiss_delete_category_alert(self):
        self.dismiss_alert()

    def click_rebuild_button(self):
        self.find_element(locator=self.rebuild_button).click()




