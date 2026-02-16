# texts.py

TEXT_HELLO = "Добро пожаловать в систему."
TEXT_GENERIC_ERROR = "Произошла ошибка. Попробуйте позже."
TEXT_MAIN_MENU = "Главное меню:"

KEYBOARD_MAIN = [
    [
        {"text": "Заявки", "callbackData": "menu_requests"},
        {"text": "Мониторинг", "callbackData": "menu_monitoring"}
    ],
    [
        {"text": "Скрипты", "callbackData": "menu_scripts"},
        {"text": "Настройка", "callbackData": "menu_settings"}
    ]
]
