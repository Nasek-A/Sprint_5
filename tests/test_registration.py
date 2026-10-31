from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from locators import (
    REGISTER_NAME_INPUT,
    REGISTER_EMAIL_INPUT,
    REGISTER_PASSWORD_INPUT,
    REGISTER_BUTTON,
    INCORRECT_PASSWORD_ERROR,
)

from config import BASE_URL

from helpers import generate_email, generate_password


class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get(BASE_URL + "register")

        driver.find_element(*REGISTER_NAME_INPUT).send_keys("Иван")
        driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys(
            generate_password()
        )

        driver.find_element(*REGISTER_BUTTON).click()

        # Ждём перехода на страницу входа
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )

        assert "/login" in driver.current_url

    def test_registration_with_short_password_shows_error(self, driver):
        driver.get(BASE_URL + "register")

        driver.find_element(*REGISTER_NAME_INPUT).send_keys("Тест")
        driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys("12345")

        driver.find_element(*REGISTER_BUTTON).click()

        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(INCORRECT_PASSWORD_ERROR)
        )

        assert error_message.is_displayed()