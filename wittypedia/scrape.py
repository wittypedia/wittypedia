import requests
import bs4
from wittypedia.gen_tools import MAIN_WIKI_URL


def scrape_url(URL):
    response = requests.get(URL)

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    links = soup.select('a')

    temp_list = [URL]
    main_list = []

    for link in links:
        if link.get('href') != None:
            if 'https://' in link.get('href'):
                temp_list.append(link.get('href'))
            else:
                temp_list.append('https://en.wikipedia.org' + link.get('href'))

    for i in temp_list:
        if i != f"{MAIN_WIKI_URL}Main_Page" and i.startswith(
                MAIN_WIKI_URL) and ":" not in i[30:]:
            main_list.append(i)

    return main_list