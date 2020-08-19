from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class MyWaits:

    def __init__(self, driver):
        self.driver = driver

    def title(self, title, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.title_is(title))
        except TimeoutException:
            raise TimeoutException(f"Ждал что title будет: {title} но он был {self.driver.title}")

    def wait_element_by_id(self, selector, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.ID, selector)))
        except TimeoutException:
            raise TimeoutException(f"Не дождался видимости элемента: {selector}")

    def wait_element_by_css(self, selector, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        except TimeoutException:
            raise TimeoutException(f"Не дождался видимости элемента: {selector}")

    def wait_element_by_link_text(self, selector, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.LINK_TEXT, selector)))
        except TimeoutException:
            raise TimeoutException(f"Не дождался видимости элемента: {selector}")

    def wait_element_by_xpath(self, selector, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, selector)))
        except TimeoutException:
            raise TimeoutException(f"Не дождался видимости элемента: {selector}")

    def wait_element_by_class_name(self, selector, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, selector)))
        except TimeoutException:
            raise TimeoutException(f"Не дождался видимости элемента: {selector}")

