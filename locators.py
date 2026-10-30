from selenium.webdriver.common.by import By

# Ссылка «Личный кабинет» в шапке сайта
PERSONAL_ACCOUNT_LINK = (By.CSS_SELECTOR, 'a[href="/account"]')

# Кнопка «Войти в аккаунт» на главной странице
LOGIN_TO_ACCOUNT_BUTTON = (
    By.XPATH,
    "//button[normalize-space()='Войти в аккаунт']"
)

# Поле «Имя» в форме регистрации
REGISTER_NAME_INPUT = (
    By.NAME,
    "name"
)

# Поле «Email» в форме регистрации
REGISTER_EMAIL_INPUT = (
    By.XPATH,
    "//fieldset[.//label[normalize-space()='Email']]//input"
)

# Поле «Пароль» в форме регистрации
REGISTER_PASSWORD_INPUT = (
    By.NAME,
    "Пароль"
)

# Кнопка «Зарегистрироваться» в форме регистрации
REGISTER_BUTTON = (
    By.XPATH,
    "//button[normalize-space()='Зарегистрироваться']"
)

# Поле «Email» на странице входа
LOGIN_EMAIL_INPUT = (
    By.XPATH,
    "//fieldset[.//label[normalize-space()='Email']]//input"
)

# Поле «Пароль» на странице входа
LOGIN_PASSWORD_INPUT = (
    By.NAME,
    "Пароль"
)

# Кнопка «Войти» на странице авторизации
LOGIN_SUBMIT_BUTTON = (
    By.XPATH,
    "//button[normalize-space()='Войти']"
)

# Ссылка «Войти» в форме регистрации
REGISTER_LOGIN_LINK = (
    By.CSS_SELECTOR,
    'a[href="/login"]'
)

# Ссылка «Восстановить пароль» на странице входа
FORGOT_PASSWORD_LINK = (
    By.CSS_SELECTOR,
    'a[href="/forgot-password"]'
)

# Ссылка «Войти» на странице восстановления пароля
RECOVERY_LOGIN_LINK = (
    By.CSS_SELECTOR,
    'a[href="/login"]'
)

# Ссылка «Конструктор» в шапке сайта
CONSTRUCTOR_LINK = (
    By.XPATH,
    "//p[normalize-space()='Конструктор']"
)

# Логотип Stellar Burgers в шапке сайта
STELLAR_BURGERS_LOGO = (
    By.XPATH,
    "//div[contains(@class, 'header__logo')]//a[@href='/']"
)

# Кнопка «Выход» в личном кабинете
LOGOUT_BUTTON = (
    By.XPATH,
    "//button[normalize-space()='Выход']"
)

# Вкладка «Булки» в конструкторе
BUNS_TAB = (
    By.XPATH,
    "//div[contains(@class, 'tab_tab')][.//span[normalize-space()='Булки']]"
)

# Вкладка «Соусы» в конструкторе
SAUCES_TAB = (
    By.XPATH,
    "//div[contains(@class, 'tab_tab')][.//span[normalize-space()='Соусы']]"
)

# Вкладка «Начинки» в конструкторе
FILLINGS_TAB = (
    By.XPATH,
    "//div[contains(@class, 'tab_tab')][.//span[normalize-space()='Начинки']]"
)

# «Некорректный пароль»
INCORRECT_PASSWORD_ERROR = (
    By.XPATH,
    "//*[normalize-space()='Некорректный пароль']"
)