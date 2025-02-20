import os
import requests
import time
from settings.config import STATUS_FILES, LENGTH_FILE, RETRIES, TIMEOUT, DELAY


def link_already_checked(url):
    for status_code, filepath in STATUS_FILES.items():
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as file:
                if url in file.read():
                    return True
    return False


class LinkChecker:
    def __init__(self):
        self.session = requests.Session()

    def check_links(self, links):
        global response
        print("Запуск проверки ссылок...")
        total_links = len(links)
        checked_links = 0

        for url in links:
            if link_already_checked(url):
                print(f'Пропущено (уже проверено): {url}')
                continue

            retries = RETRIES
            while retries > 0:
                try:
                    response = self.session.head(url, allow_redirects=True, timeout=TIMEOUT)
                    break
                except requests.exceptions.RequestException as e:
                    print(f'Ошибка при запросе {url}: {e}')
                    retries -= 1
                    if retries == 0:
                        print(f'Не удалось проверить {url}, пропускаем')
                        continue
                    time.sleep(2)

            checked_links += 1
            status_code = response.status_code
            filename = STATUS_FILES.get(str(status_code), STATUS_FILES["404"])

            with open(filename, 'a', encoding='utf-8') as file:
                file.write(url + '\n')

            if status_code == 200:
                content_length = response.headers.get('Content-Length', 'Неизвестно')
                if content_length.isdigit():
                    content_length_mb = int(content_length) / (1024 * 1024)
                    content_length_str = f'{content_length_mb:.2f} МБ'
                else:
                    content_length_str = 'Неизвестно'

                with open(LENGTH_FILE, 'a', encoding='utf-8') as length_file:
                    length_file.write(f'{url} | Размер: {content_length_str}\n')

            print(f'Проверено {checked_links}/{total_links}: {url} -> {status_code}')
            time.sleep(DELAY)

        print("Проверка завершена, ссылки сохранены по статусам HTTP.")
