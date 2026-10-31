from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    PERSONAL_ACCOUNT_LINK,
    LOGIN_EMAIL_INPUT,
    LOGIN_PASSWORD_INPUT,
    LOGIN_SUBMIT_BUTTON,
    CONSTRUCTOR_LINK,
    STELLAR_BURGERS_LOGO,
    LOGIN_TO_ACCOUNT_BUTTON,
)

from config import (
    BASE_URL,
    EMAIL,
    PASSWORD,
)


class TestPersonalAccount:

    def test_go_to_constructor_from_personal_account(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*PERSONAL_ACCOUNT_LINK).click()

        WebDriverWait(driver, 5).until(
            EC.url_contains("/login")
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

        driver.find_element(*CONSTRUCTOR_LINK).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(BASE_URL)
        )

        assert driver.current_url == BASE_URL

    def test_go_to_constructor_by_logo(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*PERSONAL_ACCOUNT_LINK).click()

        WebDriverWait(driver, 5).until(
            EC.url_contains("/login")
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

        driver.find_element(*STELLAR_BURGERS_LOGO).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(BASE_URL)
        )

        assert driver.current_url == BASE_URL

    def test_open_personal_account(self, driver):
        driver.get(BASE_URL)

        # Переходим в личный кабинет
        driver.find_element(*PERSONAL_ACCOUNT_LINK).click()

        # Проверяем переход на страницу входа
        WebDriverWait(driver, 5).until(
            EC.url_contains("/login")
        )

        assert "/login" in driver.current_url

    def test_open_personal_account_after_login(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*LOGIN_TO_ACCOUNT_BUTTON).click()

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

        assert "/account/profile" in driver.current_url