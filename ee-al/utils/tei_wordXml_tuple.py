"""
map string to its xml element for tei.
dizgeyi parçası olduğu xml etiketine eşleme işlemi

"""

# Packages / Paketler -------------------------------

import bs4
import itertools

# --------------------------------------------------

__author__ = "D. Kaan Eraslan, kaaneraslan@gmail.com"
__license__ = "GPL-3,0. See LICENSE."


# ------------------------------------------------

def tei_wordXml_t(string):
    """
    params: string, str.
    return: final_list, list of tuples

    The function takes the html page as a string, then parses
    it with BeautifulSoup. We return a list of tuples like
    [('Word','<w>Word</w>'), ...]. Every element of the final
    list of tuples is unique.

    İşlem html sayfasını dizge olarak, alıp BeautifulSoup
    aracılığıyla analiz eder. En sonunda şöyle bir tuple
    listesi sunuyoruz [('Kelime','<w>Kelime</w>'), ...].
    Listenin her elemanı özgün.

    """
    #
    parsed_string = bs4.BeautifulSoup(string, "lxml")
    find_text = parsed_string.find_all("text")
    find_words_text = [text.find_all("w", string=True) for text in find_text]
    flatten_word_list = list(itertools.chain.from_iterable(find_words_text))
    unique_word_list = list(set(flatten_word_list))
    final_word_list = []
    #
    for word_with_tag in unique_word_list:
        word = word_with_tag.get_text(" ", strip=True)
        tag_string = str(word_with_tag)
        word_tag_tuple = (word, tag_string)
        final_word_list.append(word_tag_tuple)
    #
    return final_word_list

