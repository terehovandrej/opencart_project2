import allure

from pages.admin_page import AdminPage
from pages.products_page import ProductsPage
from product_queries import ProductQueries

# --alluredir allure-report
# --allure serve allure-report


@allure.feature('feature_1')
@allure.story('epic_1')
@allure.title("Test add new product")
def test_add_new_product(login_page):
    login_page.login('user', 'bitnami1')
    admin_page = AdminPage(driver=login_page.driver)
    admin_page.go_to_products()
    products_page = ProductsPage(driver=login_page.driver)
    products_page.click_add_product_button()
    products_page.set_new_product_required_fields("iphone", "phones", "11pro")
    products_page.click_submit_button()
    assert products_page.success_alert_element
    assert ProductQueries().get_product("iphone")
    products_page.check_product_in_table('iphone')
    products_page.delete_product_from_table('iphone')
    products_page.check_product_is_not_in_table('iphone')


@allure.feature('feature_1')
@allure.story('epic_2')
@allure.title("Test add delete product")
def test_delete_product(login_page):
    ProductQueries().add_product("iphone", "11pro")
    login_page.login('user', 'bitnami1')
    admin_page = AdminPage(driver=login_page.driver)
    admin_page.go_to_products()
    products_page = ProductsPage(driver=login_page.driver)
    # products_page.click_add_product_button()
    # products_page.set_new_product_required_fields("iphone", "phones", "11pro")
    # products_page.click_submit_button()
    # assert products_page.success_alert_element
    products_page.check_product_in_table('iphone')
    products_page.delete_product_from_table('iphone')
    products_page.check_product_is_not_in_table('iphone')


@allure.feature('feature_2')
@allure.story('epic_1')
@allure.title("Test cancel delete")
def test_cancel_delete_product(login_page):
    login_page.login('user', 'bitnami1')
    admin_page = AdminPage(driver=login_page.driver)
    admin_page.go_to_products()
    products_page = ProductsPage(driver=login_page.driver)
    products_page.click_add_product_button()
    products_page.set_new_product_required_fields("iphone", "phones", "11pro")
    products_page.click_submit_button()
    assert products_page.success_alert_element
    products_page.check_product_in_table('iphone')
    products_page.delete_product_from_table('iphone')
    products_page.check_product_is_not_in_table('iphone')


@allure.feature('feature_2')
@allure.story('epic_2')
@allure.title("Test modify product")
def test_modify_product(login_page):
    ProductQueries().add_product("iphone", "11pro")
    login_page.login('user', 'bitnami1')
    admin_page = AdminPage(driver=login_page.driver)
    admin_page.go_to_products()
    products_page = ProductsPage(driver=login_page.driver)
    # products_page.click_add_product_button()
    # products_page.set_new_product_required_fields("iphone", "phones", "11pro")
    # products_page.click_submit_button()
    # assert products_page.success_alert_element
    products_page.click_edit_button('iphone')
    products_page.set_new_product_required_fields("samsung", "phones", "s20")
    products_page.click_submit_button()
    assert products_page.success_alert_element
    assert ProductQueries().get_product("samsung")
    ProductQueries().check_product_deleted("iphone", "11pro")
    products_page.check_product_in_table('samsung')
    products_page.check_product_is_not_in_table('iphone')
    products_page.delete_product_from_table('samsung')
    products_page.check_product_is_not_in_table('samsung')

