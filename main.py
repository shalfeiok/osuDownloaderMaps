from generator import LinkGenerator
from checker import LinkChecker
from downloader import FileDownloader


def main():
    # Генерация ссылок
    generator = LinkGenerator()
    links = generator.generate_links()

    # Проверка ссылок
    checker = LinkChecker()
    checker.check_links(links)

    # Загрузка файлов
    downloader = FileDownloader()
    downloader.download_files()


if __name__ == "__main__":
    main()
