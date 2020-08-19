import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from selenium.webdriver import ChromeOptions


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--start-maximized")
        wd = webdriver.Chrome(options=options)
    # if browser_name == "chrome":
    #     # caps = {
    #     #     "browserName": "chrome",
    #     #     "version": "83.0",
    #     #     "enableVNC": True,
    #     #     "enableVideo": True,
    #     #     "acceptSslCerts": True,
    #     #     "acceptInsecureCerts": True
    #     # }
    #     # executor_url = "http://localhost:4444/wd/hub"
    #     # wd = webdriver.Remote(command_executor=executor_url, desired_capabilities=caps)
    #
    elif browser_name == "firefox":
        caps = {
            "browserName": "firefox",
            "version": "77.0",
            "enableVNC": True,
            "enableVideo": True
        }
        executor_url = "http://localhost:4444/wd/hub"
        wd = webdriver.Remote(command_executor=executor_url, desired_capabilities=caps)
    else:
        raise pytest.UsageError("browser should be chrome or firefox")
    yield wd
    wd.quit()


@pytest.fixture()
def login_page(browser):
    page = LoginPage(browser)
    page.go_to()
    return page


@pytest.fixture()
def main_page(browser):
    page = MainPage(browser)
    page.go_to()
    return page


@pytest.fixture(scope="function")
def base_url(request):
    return request.config.getoption("--url")


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help="Choose browser: chrome or firefox")
    parser.addoption(
        '--url',
        action='store',
        default='http://192.168.1.1/',
        help='This is base url'
    )
