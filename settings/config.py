import os

# Пути к файлам
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETTINGS_DIR = os.path.join(BASE_DIR, 'settings')

STATUS_FILES = {
    "200": os.path.join(SETTINGS_DIR, "200.txt"),
    "404": os.path.join(SETTINGS_DIR, "404.txt"),
    "301": os.path.join(SETTINGS_DIR, "301.txt"),
    "302": os.path.join(SETTINGS_DIR, "302.txt"),
    "403": os.path.join(SETTINGS_DIR, "403.txt"),
    "500": os.path.join(SETTINGS_DIR, "500.txt"),
}

LENGTH_FILE = os.path.join(SETTINGS_DIR, "length.txt")
DOWNLOAD_DIR = r"E:\osumaps"

# Настройки для проверки ссылок
START_NUMBER = 1
END_NUMBER = 1580
RETRIES = 3
TIMEOUT = 10
DELAY = 0.5
