from bs4 import BeautifulSoup
# from googletrans import Translator
# from goslate import Goslat
from translatepy.translators.bing import BingTranslate

import requests
# from requests.adapters import HTTPAdapter
# from urllib3.util import Retry

# session = requests.Session()
# retry = Retry(connect=5, backoff_factor=0.5)
# adapter = HTTPAdapter(max_retries=retry)
# session.mount('http://', adapter)
# session.mount('https://', adapter)


def translate_html(path, lang):

    page_html = requests.get(f"http://wittypedia.herokuapp.com/{path}")
    page_html_text = page_html.text
    soup = BeautifulSoup(page_html_text, "html.parser")
    # nice_html = soup.prettify()
    # gs = Goslate()
    bingtranslator = BingTranslate()
    for i in soup.find_all("a")[:-7]:
        if i.text:
            i.string = bingtranslator.translate(
                text=i.text, destination_language=lang).result

    # return translator.translate_html(nice_html, lang)

    # print(soup.p)
    # for i in soup.find_all("a"):
    #     soup.a = translator.translate(i, dest = lang)
    nice_html = soup.prettify()
    return nice_html
