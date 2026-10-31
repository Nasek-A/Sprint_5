from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    LOGIN_TO_ACCOUNT_BUTTON,
    PERSONAL_ACCOUNT_LINK,
    LOGIN_EMAIL_INPUT,
    LOGIN_PASSWORD_INPUT,
    LOGIN_SUBMIT_BUTTON,
    REGISTER_LOGIN_LINK,
    FORGOT_PASSWORD_LINK,
    RECOVERY_LOGIN_LINK,
)

from config import (
    BASE_URL,
    EMAIL,
    PASSWORD,
)


class TestLogin:

    def test_login_from_main_page(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*LOGIN_TO_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)
        )

        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

        # Ждём перехода на главную страницу конструктора
        WebDriverWait(driver, 10).until(
            EC.url_to_be(BASE_URL)
        )

        assert driver.current_url == BASE_URL

    def test_login_from_personal_account(self, driver):
        driver.get(BASE_URL)

        # Переходим в личный кабинет
        driver.find_element(*PERSONAL_ACCOUNT_LINK).click()

        # Ждём появления поля Email на странице входа
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)
        )

        # Вводим данные зарегистрированного пользователя
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

        # Проверяем переход на главную страницу
        WebDriverWait(driver, 10).until(
            EC.url_to_be(BASE_URL)
        )

        assert driver.current_url == BASE_URL

    def test_login_from_registration_page(self, driver):
        driver.get(BASE_URL + "register")

        # Переходим к форме входа
        driver.find_element(*REGISTER_LOGIN_LINK).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)
        )

        # Вводим данные пользователя
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

        # Проверяем успешный вход
        WebDriverWait(driver, 10).until(
            EC.url_to_be(BASE_URL)
        )

        assert driver.current_url == BASE_URL

    def test_open_password_recovery_page(self, driver):
        driver.get(BASE_URL + "login")

        driver.find_element(*FORGOT_PASSWORD_LINK).click()

        WebDriverWait(driver, 5).until(
            EC.url_contains("/forgot-password")
        )

        assert "/forgot-password" in driver.current_url

    def test_login_from_password_recovery_page(self, driver):
        driver.get(BASE_URL + "forgot-password")

        # Переходим к форме входа
        driver.find_element(*RECOVERY_LOGIN_LINK).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)
        )

        # Вводим данные пользователя
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(PASSWORD)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

        # Проверяем успешный вход
        WebDriverWait(driver, 10).until(
            EC.url_to_be(BASE_URL)
        )

        assert driver.current_url == BASE_URL