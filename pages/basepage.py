import logging

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://192.168.1.69/admin/" #127.0.0.1/admin/
        # driver.execute_script("console.warn('Here is the WARNING message!')")
        # driver.execute_script("console.error('Here is the ERROR message!')")
        # driver.execute_script("console.log('Here is the LOG message!')")
        self.handler = logging.FileHandler(filename=f"{type(self).__name__}.log")
        self.formatter = logging.Formatter(fmt="%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s")
        self.handler.setFormatter(fmt=self.formatter)
        self.logger = logging.getLogger(name=type(self).__name__)
        self.logger.setLevel(level=logging.INFO)
        self.logger.addHandler(hdlr=self.handler)

    def find_element(self, locator, time=10):
        self.logger.info("Trying find element")
        try:
            return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                          message=f"Can't find element by locator {locator}")
        except TimeoutException:
            self.logger.error(f"Can't find element by locator {locator}")
            self.logger.error(f'Caught {TimeoutException.__name__}:\n{TimeoutException}')
            self.logger.error(f'Saving screenshot to {TimeoutException.__name__}.png')
            self.driver.save_screenshot(filename='TimeoutException.png')
            allure.attach(body=self.driver.get_screenshot_as_png(),
                          name="screenshot_image",
                          attachment_type=allure.attachment_type.PNG)

    def find_element_by_xpath(self, selector, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located((By.XPATH, selector)),
                                                      message=f"Can't find elements by locator {selector}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def test_element_does_not_present(self, locator, time=3):
        try:
            WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return True
        return False

    def accept_alert(self):
        Alert(self.driver).accept()

    def dismiss_alert(self):
        Alert(self.driver).dismiss()

    def go_to(self):
        return self.driver.get(self.base_url)
