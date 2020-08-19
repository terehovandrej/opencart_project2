from selenium.webdriver.common.by import By
from .basepage import BasePage


class LoginPage(BasePage):

    username = (By.ID, 'input-username')
    password = (By.ID, 'input-password')
    submit_button = (By.CSS_SELECTOR, 'button')
    login_button = (By.XPATH, '//button[@type="submit"]')
    container_fluid = (By.CLASS_NAME, "container-fluid")
    bar_static_top = (By.CLASS_NAME, "navbar-static-top")
    col_sm_offset = (By.CLASS_NAME, "col-sm-offset-4")
    panel_default = (By.CLASS_NAME, "panel-default")
    panel_title = (By.CLASS_NAME, "panel-title")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def _set_username_(self, name):
        self.find_element(locator=self.username).clear()
        self.find_element(locator=self.username).send_keys(name)

    def _set_password_(self, password):
        self.find_element(locator=self.password).clear()
        self.find_element(locator=self.password).send_keys(password)

    def login(self, username, password):
        self._set_username_(username)
        self._set_password_(password)
        self.find_element(locator=self.submit_button).click()

    @property
    def login_button_element(self):
        return self.find_element(self.login_button)

    @property
    def container_fluid_element(self):
        return self.find_element(self.container_fluid)

    @property
    def bar_static_top_element(self):
        return self.find_element(self.bar_static_top)

    @property
    def col_sm_offset_element(self):
        return self.find_element(self.col_sm_offset)

    @property
    def panel_default_element(self):
        return self.find_element(self.panel_default)

    @property
    def panel_title_element(self):
        return self.find_element(self.panel_title)

    def check_login_page_elements(self):
        assert self.container_fluid_element
        assert self.bar_static_top_element
        assert self.col_sm_offset_element
        assert self.panel_default_element
        assert self.panel_title_element

    def write_logs(self, log_type):
        browser = self.driver.get_log(log_type)
        for l in browser:
            print(l)
