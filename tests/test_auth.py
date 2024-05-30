import time

from urllib3.util import url

from pages.auth_page import AuthPage
from tests.conftest import is_valid_url


def test_auth_page_with_incorrect_data(driver):
    page = AuthPage(driver)
    page.enter_email("6584616156")
    page.enter_pass("56df6ER65")
    page.btn_click()
    time.sleep(5)
    error_element = page.per()
    assert error_element.is_displayed()
    is_valid = is_valid_url(url)
    print(is_valid)



    # assert page.get_relative_link() != '/all_pets', "login error"
