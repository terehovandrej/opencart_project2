from selenium.webdriver.common.by import By

from .basepage import BasePage


class MainPage(BasePage):
    top = (By.ID, 'top')
    common_home = (By.ID, "common-home")
    top_links = (By.ID, "top-links")
    menu = (By.ID, "menu")
    form_currency = (By.ID, "form-currency")

    input_quantity = (By.CSS_SELECTOR, "#input-quantity")
    button_cart = (By.CSS_SELECTOR, "#button-cart")
    add_this = (By.CSS_SELECTOR, "a.addthis_button_expanded")
    button_add_to_wish_list = (By.CSS_SELECTOR, "button[data-original-title='Add to Wish List']")
    button_compare = (By.CSS_SELECTOR, "button[data-original-title='Compare this Product']")

    my_account = (By.LINK_TEXT, "My Account")
    register = (By.LINK_TEXT, "Register")
    login = (By.LINK_TEXT, "Login")
    order_history = (By.LINK_TEXT, "Order History")
    downloads = (By.LINK_TEXT, "Downloads")

    wish_list_button = (By.XPATH, "//button[@data-original-title='Add to Wish List']")
    compare_product_button = (By.XPATH, "//button[@data-original-title='Compare this Product']")
    add_to_cart = (By.XPATH, "//span[text()='Add to Cart']")
    cart_total = (By.XPATH, "//span[@id='cart-total']/..")
    phones_and_pda = (By.XPATH, "//a[text()='Phones & PDAs']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.base_url = "https://localhost"

    @property
    def top_element(self):
        return self.find_element(self.top)

    @property
    def common_home_element(self):
        return self.find_element(self.common_home)

    @property
    def top_links_element(self):
        return self.find_element(self.top_links)

    @property
    def menu_element(self):
        return self.find_element(self.menu)

    @property
    def form_currency_element(self):
        return self.find_element(self.form_currency)

    @property
    def my_account_element(self):
        return self.find_element(self.my_account)

    @property
    def register_element(self):
        return self.find_element(self.register)

    @property
    def login_element(self):
        return self.find_element(self.login)

    @property
    def order_history_element(self):
        return self.find_element(self.order_history)

    @property
    def downloads_element(self):
        return self.find_element(self.downloads)

    @property
    def input_quantity_element(self):
        return self.find_element(self.input_quantity)

    @property
    def button_cart_element(self):
        return self.find_element(self.button_cart)

    @property
    def add_this_element(self):
        return self.find_element(self.add_this)

    @property
    def button_add_to_wish_list_element(self):
        return self.find_element(self.button_add_to_wish_list)

    @property
    def button_compare_element(self):
        return self.find_element(self.button_compare)

    @property
    def wish_list_button_element(self):
        return self.find_element(self.wish_list_button)

    @property
    def compare_product_button_element(self):
        return self.find_element(self.compare_product_button)

    @property
    def add_to_cart_element(self):
        return self.find_element(self.add_to_cart)

    @property
    def cart_total_element(self):
        return self.find_element(self.cart_total)

    @property
    def phones_and_pda_element(self):
        return self.find_element(self.phones_and_pda)

    def check_elements_on_product_card(self):
        self.driver.get(
            "http://192.168.1.69/index.php?route=product/product&search=%D0%90%D0%B9%D1%84%D0%BE%D0%BD&product_id=89")
        assert self.input_quantity_element
        assert self.button_cart_element
        assert self.add_this_element
        assert self.button_add_to_wish_list_element
        assert self.button_compare_element

    def check_elements_on_login_page(self):
        self.driver.get("http://192.168.1.69/index.php?route=account/login")
        assert self.my_account_element
        assert self.register_element
        assert self.login_element
        assert self.order_history_element
        assert self.downloads_element

    def check_elements_on_main_page(self):
        assert self.top_element
        assert self.common_home_element
        assert self.top_links_element
        assert self.menu_element
        assert self.form_currency_element

    def check_catalog_elements(self):
        self.driver.get(
            "http://192.168.1.69/index.php?route=product/search&search=%D0%B0%D0%B9%D1%84%D0%BE%D0%BD")
        assert self.wish_list_button_element
        assert self.compare_product_button_element
        assert self.add_to_cart_element
        assert self.cart_total_element
        assert self.phones_and_pda_element
