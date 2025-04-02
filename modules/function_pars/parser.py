# Импорт для создания запросов на сайты/апи
import requests as request
# Модуль который позволит нам парсить данные
import bs4 
# Импорт класса для создания html label
from ..GUI.classes.html_label import HtmlLabel 

async def auto_parser(url: str, parse_mode: str, frame_dict: dict, target: str = None):
    '''
    #### Асинхронная функция для парсинга данных с сайта ####

    Параметры:
    url: str - адрес сайта для парсинга
    target: str - теги которые будут извлечены из html
    parse_mode: str - режим парсинга ('all' - все теги, 'first' - первый тег)
    '''
    # Используем операторы try except 
    try:
        # Выполняем запрос к сайту и получаем ответ
        response = request.get(url = url)
        # Проверяем, если запрос был успешным, то парсим данные
        if response.status_code == 200:
            # Если режим парсинга 'all', то парсим все теги и выводим их в виде html
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            # Если флаг стоит all
            if parse_mode == 'all':
                # Парсим ВСЕ данные
                data_html = soup.find_all()[:200]
                # Создаем HtmlLabel с данными
                html_label = HtmlLabel(
                    ch_master = frame_dict["HEADER"],
                    ch_html_text = data_html[0],
                    ch_width = 150,
                    ch_height = 150,
                    ch_fg_color = '#ffffff',
                    ch_text_color = '#000000',
                    ch_relief = 'groove',
                    ch_borderwidth = 3,
                )
                print(f'Это текст который мы размещаем: {data_html}')
                # Размещаем
                html_label.pack()
                
            # В другом случае ищем конкретнные блоки
            headers = soup.find_all(target)
            # Возвращаем найденные блоки
            return headers
        # Если код не 200
        else:
            print(f'Ошибка при парсинге данных, код ошибки: {response.status_code}')
    # Отлавливаем ошибку и выводим
    except Exception as error:
        print(f"Error occurred while fetching the URL: {error}")
        return str(error)

# asyncio.run(main = auto_parser(url = "https://my.testportal.gov.ua/cabinet/login", parse_mode = "all"))