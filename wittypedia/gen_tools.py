# any helper functions in logic and constants are defined here
import urllib.parse
from urllib import response
import requests
import wikipedia

MAIN_WIKI_URL = "https://en.wikipedia.org/wiki/"


def setify_in_order(list1):
    set_list = []
    for i in list1:
        if i not in set_list:
            set_list.append(i)

    return set_list


def wiki_links_fmt(links_list):
    formatted = []
    for i, j in enumerate(links_list):
        unbuilt_topic = urllib.parse.unquote(j[30:])
        # images = get_images(unbuilt_topic)
        formatted.append((i + 1, unbuilt_topic.replace("_", " "), j))

    return formatted


def search_results_fmt(results_list):
    formatted = []
    for i in range(len(results_list)):
        to_quote = results_list[i].encode("utf-8")
        built_url = MAIN_WIKI_URL + urllib.parse.quote(to_quote)
        # try:
        #     images = get_images(results_list[i])
        # except:
        #     images = []
        formatted.append((i + 1, results_list[i], built_url))

    return formatted


def randomize_topic():
    randompages = wikipedia.random(pages=5)
    random_topic = ""

    for i in randompages:
        try:
            link = wikipedia.page(i).url
        except:
            pass

        response = requests.get(link)

        if response.status_code == 200:
            random_topic = i
            break
        else:
            pass

    return random_topic


def get_images(topic):
    return wikipedia.page(topic).images