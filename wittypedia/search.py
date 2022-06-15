from fuzzywuzzy import fuzz
import wikipedia


def search_wiki(topic, num_results):
    return wikipedia.search(topic, results=num_results)


LEVENSHTEIN_EPSILON = 80


def fuzzy_search(query, str_list):
    results_of_search = []
    for i in str_list:
        if fuzz.partial_ratio(query.upper(), i.upper()) > LEVENSHTEIN_EPSILON:
            results_of_search.append(i)

    return results_of_search
