import requests as request
import bs4 
import asyncio



async def auto_parser(url: str):
    
    try:
        response = request.get(url = url)
        if response.status_code == 200:
            soup = bs4.BeautifulSoup(response.text, 'html.parser')

            headers = soup.find_all('h1')
            print(f'Это хедеры{ headers}')
            
    except Exception as error:
        print(f"Error occurred while fetching the URL: {error}")
        return str(error)

asyncio.run(main = auto_parser(url = "https://quoцtes.toscrape.com/"))