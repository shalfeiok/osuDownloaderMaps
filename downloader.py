import os
import requests
from settings.config import STATUS_FILES, DOWNLOAD_DIR


class FileDownloader:
    def __init__(self):
        self.download_dir = DOWNLOAD_DIR
        os.makedirs(self.download_dir, exist_ok=True)

    def _get_file_size(self, response):
        try:
            return int(response.headers.get('Content-Length', 0))
        except ValueError:
            return 0

    def _human_readable_size(self, size):
        for unit in ['Б', 'КБ', 'МБ', 'ГБ']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} ТБ"

    def _show_progress(self, downloaded, total):
        if total > 0:
            percent = downloaded / total * 100
            bar_length = 40
            filled_length = int(bar_length * downloaded // total)
            bar = '█' * filled_length + '-' * (bar_length - filled_length)
            print(
                f'\r|{bar}| {percent:.1f}% ({self._human_readable_size(downloaded)} / {self._human_readable_size(total)})',
                end='')
        else:
            print(f'\rЗагружено: {self._human_readable_size(downloaded)}', end='')

    def download_files(self):
        print("\nЗапуск загрузки файлов...")
        if not os.path.exists(STATUS_FILES["200"]) or os.stat(STATUS_FILES["200"]).st_size == 0:
            print("Файл 200.txt пуст, загрузка невозможна.")
            return

        with open(STATUS_FILES["200"], "r", encoding="utf-8") as file:
            links = [line.strip() for line in file.readlines()]

        if not links:
            print("Нет ссылок для загрузки.")
            return

        print(f"Найдено {len(links)} ссылок для загрузки.\n")

        for link in links:
            # print(f"[Обработка] {link}")
            try:
                number = int(link.split("S")[1].split("%20")[0])
            except (IndexError, ValueError):
                print(f"⚠️ Не удалось извлечь номер из {link}, пропускаем...")
                continue

            new_filename = f"S{number}.7z"
            filepath = os.path.join(self.download_dir, new_filename)

            if os.path.exists(filepath):
                print(f"✅ Файл {new_filename} уже существует, пропускаем...\n")
                continue

            print(f"⬇️ Начало загрузки: {new_filename}")
            try:
                with requests.get(link, stream=True) as response:
                    response.raise_for_status()
                    total_size = self._get_file_size(response)
                    downloaded = 0

                    with open(filepath, "wb") as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
                                downloaded += len(chunk)
                                self._show_progress(downloaded, total_size)

                    print(f"\n✅ Успешно: {new_filename} ({self._human_readable_size(downloaded)})")
                    print("-" * 50)

            except requests.exceptions.RequestException as e:
                print(f"\n❌ Ошибка загрузки {new_filename}: {e}")
                if os.path.exists(filepath):
                    os.remove(filepath)

        print("\nВсе доступные файлы обработаны.")
