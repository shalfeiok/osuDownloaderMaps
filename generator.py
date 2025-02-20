from settings.config import START_NUMBER, END_NUMBER

class LinkGenerator:
    @staticmethod
    def generate_links():
        print("Генерация ссылок...")
        links = []
        for number in range(START_NUMBER, END_NUMBER + 1):
            for archive in ["zip", "7z"]:
                for osuerr in ["", "%20osu%21"]:
                    if osuerr:
                        url = f'https://packs.ppy.sh/S{number}%20-%20osu%21%20Beatmap%20Pack%20%23{number}.{archive}'
                    else:
                        url = f'https://packs.ppy.sh/S{number}%20-%20Beatmap%20Pack%20%23{number}.{archive}'
                    links.append(url)
        print(f"Сгенерировано {len(links)} ссылок.")
        return links
