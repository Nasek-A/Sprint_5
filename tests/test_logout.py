from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    PERSONAL_ACCOUNT_LINK,
    LOGIN_EMAIL_INPUT,
    LOGIN_PASSWORD_INPUT,
    LOGIN_SUBMIT_BUTTON,
    LOGOUT_BUTTON,
)

from config import (
    BASE_URL,
    EMAIL,
    PASSWORD,
)


def test_logout_from_personal_account(driver):
    driver.get(BASE_URL)

    driver.find_element(*PERSONAL_ACCOUNT_LINK).click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)
    )

    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(EMAIL)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(PASSWORD)
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be(BASE_URL)
    )

    driver.find_element(*PERSONAL_ACCOUNT_LINK).click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/account/profile")
    )

    driver.find_element(*LOGOUT_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )

    assert "/login" in driver.current_url
