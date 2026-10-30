from selenium.webdriver.support.ui import WebDriverWait

from config import BASE_URL

from locators import (
    LOGIN_TO_ACCOUNT_BUTTON,
    BUNS_TAB,
    SAUCES_TAB,
    FILLINGS_TAB,
)


def test_login_to_account_button_exists(driver):
    driver.get(BASE_URL)

    button = driver.find_element(*LOGIN_TO_ACCOUNT_BUTTON)

    assert button.is_displayed()
    assert button.text == "Войти в аккаунт"


def test_buns_tab_is_selected_by_default(driver):
    driver.get(BASE_URL)

    buns_tab = driver.find_element(*BUNS_TAB)

    assert "tab_tab_type_current" in buns_tab.get_attribute("class")


def test_sauces_tab_can_be_selected(driver):
    driver.get(BASE_URL)

    driver.find_element(*SAUCES_TAB).click()

    WebDriverWait(driver, 5).until(
        lambda d: "tab_tab_type_current"
        in d.find_element(*SAUCES_TAB).get_attribute("class")
    )

    assert "tab_tab_type_current" in driver.find_element(
        *SAUCES_TAB
    ).get_attribute("class")


def test_fillings_tab_can_be_selected(driver):
    driver.get(BASE_URL)

    driver.find_element(*FILLINGS_TAB).click()

    WebDriverWait(driver, 5).until(
        lambda d: "tab_tab_type_current"
        in d.find_element(*FILLINGS_TAB).get_attribute("class")
    )

    assert "tab_tab_type_current" in driver.find_element(
        *FILLINGS_TAB
    ).get_attribute("class")


def test_buns_tab_can_be_selected(driver):
    driver.get(BASE_URL)

    # Сначала выбираем «Соусы»
    driver.find_element(*SAUCES_TAB).click()

    WebDriverWait(driver, 5).until(
        lambda d: "tab_tab_type_current"
        in d.find_element(*SAUCES_TAB).get_attribute("class")
    )

    # Возвращаемся к «Булкам»
    driver.find_element(*BUNS_TAB).click()

    WebDriverWait(driver, 5).until(
        lambda d: "tab_tab_type_current"
        in d.find_element(*BUNS_TAB).get_attribute("class")
    )

    assert "tab_tab_type_current" in driver.find_element(
        *BUNS_TAB
    ).get_attribute("class")
