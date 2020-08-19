

def test_browser_logging(login_page):
    login_page.write_logs('performance')
    login_page.write_logs('browser')
