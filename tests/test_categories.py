from pages.admin_page import AdminPage
from pages.categories_page import CategoriesPage


def test_add_new_category(login_page):
    login_page.login('user', 'bitnami1')
    admin_page = AdminPage(driver=login_page.driver)
    admin_page.go_to_categories()
    categories_page = CategoriesPage(driver=login_page.driver)
    categories_page.click_add_category_button()
    categories_page.set_category_required_fields("1test category", "tag")
    categories_page.click_submit_button()
    assert categories_page.success_alert_element
    categories_page.check_category_in_table('1test category')
    categories_page.delete_category_from_table('1test category')
    categories_page.accept_delete_category_alert()
    categories_page.check_category_is_not_in_table('1test category')


def test_delete_category(login_page):
    login_page.login('user', 'bitnami1')
    admin_page = AdminPage(driver=login_page.driver)
    admin_page.go_to_categories()
    categories_page = CategoriesPage(driver=login_page.driver)
    categories_page.click_add_category_button()
    categories_page.set_category_required_fields("1test category", "tag")
    categories_page.click_submit_button()
    assert categories_page.success_alert_element
    categories_page.check_category_in_table('1test category')
    categories_page.delete_category_from_table('1test category')
    categories_page.accept_delete_category_alert()
    categories_page.check_category_is_not_in_table('1test category')


def test_modify_category(login_page):
    login_page.login('user', 'bitnami1')
    admin_page = AdminPage(driver=login_page.driver)
    admin_page.go_to_categories()
    categories_page = CategoriesPage(driver=login_page.driver)
    categories_page.click_add_category_button()
    categories_page.set_category_required_fields("1test category", "tag")
    categories_page.click_submit_button()
    assert categories_page.success_alert_element
    categories_page.check_category_in_table('1test category')
    categories_page.click_edit_button('1test category')
    categories_page.set_category_required_fields("2test category", "tag")
    categories_page.click_submit_button()
    assert categories_page.success_alert_element
    categories_page.check_category_in_table('2test category')
    categories_page.delete_category_from_table('2test category')
    categories_page.accept_delete_category_alert()
    categories_page.check_category_is_not_in_table('2test category')


def test_rebuild_category(login_page):
    login_page.login('user', 'bitnami1')
    admin_page = AdminPage(driver=login_page.driver)
    admin_page.go_to_categories()
    categories_page = CategoriesPage(driver=login_page.driver)
    categories_page.click_rebuild_button()
    assert categories_page.success_alert_element


def test_cancel_delete_category(login_page):
    login_page.login('user', 'bitnami1')
    admin_page = AdminPage(driver=login_page.driver)
    admin_page.go_to_categories()
    categories_page = CategoriesPage(driver=login_page.driver)
    categories_page.click_add_category_button()
    categories_page.set_category_required_fields("1test category", "tag")
    categories_page.click_submit_button()
    assert categories_page.success_alert_element
    categories_page.check_category_in_table('1test category')
    categories_page.delete_category_from_table('1test category')
    categories_page.dismiss_delete_category_alert()
    categories_page.check_category_in_table('1test category')
    categories_page.delete_category_from_table('1test category')
    categories_page.dismiss_delete_category_alert()
