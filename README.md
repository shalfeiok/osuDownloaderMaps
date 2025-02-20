# osuDownloaderMaps
Значит работает все это так:
  Генерирует ссылки на паки, не парсит а генерирует, опытным путём разобрался что некоторые ссылки на битмаппаки отличаются и по этому у каждой ссылки есть 4 варианта один из них и есть рабочий.
  Когда после генерации ссылок проверяет есть ли они в файлах 200.txt и 400.txt, если нет то идёт по ним запрос на сервер и получаем ответ 404 страница несуществует или 200 что все гуд и записываем в файл 200.txt или 404.txt.
  Когда мы получили ответ 200 или 404 не важно, результат записывается в файл 200.txt или 404.txt чтобы в дальнейшем не делать лишних запросов.
  После того как мы прочекали все ссылки в диапазоне от 1 до 1580 (настройки в config.py) то мы качаем файлы по очереди по ссылкам ил файла 200.txt.
  Перед загрузкой проверяет деректорию, если такой архив уже есть то не качаем а пропускаем.
  После загрузки сразу переименовывает так как получает название файла не пригодным для чтения.
Как то так.
все настройки в файле config.py в паке settings.

в консоли пишем pip install requests
запускать main.py



So it all works like this: Generates links to packs, and does not parse sequentially, empirically figured out that some links to bitmaps have a format, and for each link there are 4 manuals, one of them is the working one. When after forming requests subsequently are they in the files 200.txt and 400.txt, if not then a request to the server goes through them and receives a response 404 the page is saved or 200 that everything is good and we write it to the file 200.txt or 404.txt. When we received the answer 200 or 404, it does not matter, the result is written to the file 200.txt or 404.txt, so as not to make unnecessary requests in the future. After we checked all the links in fragments from 1 to 1580 (settings in config.py), then we download the files in turn by links or file 200.txt. Before downloading, first the directory, if such an archive already exists, then do not download, skip. After downloading, it is immediately renamed, since it receives a file name that is unsuitable for reading. Something like that. all settings in the config.py file in the settings pack.

in the console, we write requests for installing pip, run main.py
