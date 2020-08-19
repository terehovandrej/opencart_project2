def test_main_page_elements(main_page):
    main_page.check_elements_on_main_page()
    main_page.check_elements_on_login_page()
    main_page.check_elements_on_product_card()
    main_page.check_catalog_elements()


def test_admin_login_elements(login_page):
    login_page.check_login_page_elements()

