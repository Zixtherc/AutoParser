import requests as request
import bs4 
import asyncio



async def auto_parser(url: str, parse_mode: str, target: str = None):
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
                data_html = soup.get_text()
                print(f'ЭТо то что мы спарсили: {data_html}')

            headers = soup.find_all(target)
            print(f'Это хедеры{ headers}')
        else:
            print(f'Ошибка при парсинге данных, код ошибки: {response.status_code}')
    except Exception as error:
        print(f"Error occurred while fetching the URL: {error}")
        return str(error)

asyncio.run(main = auto_parser(url = "https://my.testportal.gov.ua/cabinet/login", parse_mode = "all"))