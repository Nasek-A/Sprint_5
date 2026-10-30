# Sprint_5 — Автотесты Stellar Burgers

Проект содержит автоматизированные тесты для проверки функциональности сайта [Stellar Burgers](https://stellarburgers.education-services.ru/).

## Используемые технологии

- Python
- Selenium WebDriver
- pytest
- Google Chrome

## Установка зависимостей

Установи необходимые библиотеки командой:

```bash
py -m pip install -r requirements.txt
```

## Запуск тестов

Запустить все тесты:

```bash
py -m pytest -v
```

Запустить тесты отдельного файла:

```bash
py -m pytest tests/test_login.py -v
```

Запустить тесты регистрации:

```bash
py -m pytest tests/test_registration.py -v
```

## Структура проекта

- `config.py` — настройки проекта: адрес сайта и данные тестового аккаунта.
- `conftest.py` — фикстура для создания и закрытия браузера.
- `locators.py` — локаторы элементов сайта.
- `helpers.py` — вспомогательные функции для генерации email и пароля.
- `requirements.txt` — список зависимостей проекта.
- `tests/test_constructor_sections.py` — проверка кнопки входа и вкладок конструктора.
- `tests/test_registration.py` — тесты регистрации, включая проверку ошибки при коротком пароле.
- `tests/test_login.py` — тесты входа и переходов к форме авторизации.
- `tests/test_logout.py` — проверка выхода из аккаунта.
- `tests/test_personal_account.py` — проверка переходов в личный кабинет и из него в конструктор.

## Браузер

Тесты запускаются в Google Chrome с использованием Selenium WebDriver.