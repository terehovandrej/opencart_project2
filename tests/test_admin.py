from pages.admin_page import AdminPage
from pages.products_page import ProductsPage


def test_admin_login(login_page):
    login_page.login('user', 'bitnami1')
    admin_page = AdminPage(driver=login_page.driver)
    assert admin_page.user_profile_element


def test_admin_logout(login_page):
    login_page.login('user', 'bitnami1')
    admin_page = AdminPage(driver=login_page.driver)
    admin_page.logout()
    assert login_page.login_button_element


def test_go_to_products(login_page):
    login_page.login('user', 'bitnami1')
    admin_page = AdminPage(driver=login_page.driver)
    admin_page.go_to_products()
    products_page = ProductsPage(driver=login_page.driver)
    assert products_page.main_table_element



