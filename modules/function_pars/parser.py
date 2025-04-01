import requests as request
import bs4 
import asyncio
import customtkinter as ctk

from ..GUI.classes.html_label import HtmlLabel 

async def auto_parser(url: str, parse_mode: str, frame_dict: dict, target: str = None):
    '''
    #### Асинхронная функция для парсинга данных с сайта ####

    Параметры:
    url: str - адрес сайта для парсинга
    target: str - теги которые будут извлечены из html
    parse_mode: str - режим парсинга ('all' - все теги, 'first' - первый тег)
    '''
    try:
        response = request.get(url = url)
        if response.status_code == 200:
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            if parse_mode == 'all':

                data_html = soup.prettify()
                print(f'Это дата html: {data_html}')
                html_label = HtmlLabel(
                    ch_master = frame_dict["HEADER"],
                    ch_html_text = data_html,
                    ch_width = 150,
                    ch_height = 150,
                    ch_fg_color = '#ffffff',
                    ch_text_color = '#000000',
                    ch_relief = 'groove',
                    ch_borderwidth = 3,
                )
                html_label.pack()
                

            headers = soup.find_all(target)
            # print(f'Это хедеры{ headers}')
            return headers
        else:
            print(f'Ошибка при парсинге данных, код ошибки: {response.status_code}')
    except Exception as error:
        print(f"Error occurred while fetching the URL: {error}")
        return str(error)

# asyncio.run(main = auto_parser(url = "https://my.testportal.gov.ua/cabinet/login", parse_mode = "all"))