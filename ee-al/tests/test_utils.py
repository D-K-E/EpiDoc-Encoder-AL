"""
Tests for non corpora specific functions

Belirli bir külliyata ait olmayan işlemler için testler

"""

# Paketler / Packages --------------------------

import unittest
import bs4
import itertools
from ee-al.utils.tei_wordXml_tuple import tei_wordXml_t


# ----------------------------------------------

__author__ = "D. Kaan Eraslan, kaaneraslan@gmail.com"
__license__ = "GPL-3,0. See LICENSE."

# -----------------------------------------------

class TestFunctions(unittest.TestCase):
    """
    test functions

    test işlemleri
    """
    #
    def test_tei_text_to_word_markUp_tuple_list(self):
        """
        test for tei_wordXml_t which harvest words from tei-xml.

        tei_wordXml_t işlemi için test. İşlem tei-xml halindeki
        metinden kelimeleri toplayandır
        """
        #
        with open("test_text_tei_wordXml_t.txt","r", encoding="utf-8") as test_text:
            test_string = test_text.read()
        test_tei_wordXml = tei_wordXml_t(test_string)
        comparison_text = [('GAL-ú',
  '<w corresp="#akk-seg-3" function="akkAdj" lemma="dannum">GAL-ú</w>'),
 ('(I)da-ri-ia-a-muš',
  '<w corresp="#akk-seg-1" function="akkNP" lemma="Darius">(I)da-ri-ia-a-muš</w>'),
 ('LUGAL',
  '<w corresp="#akk-seg-2" function="akkNom" lemma="šarrum" lemmaref="http://oracc.museum.upenn.edu/saao/cbd/akk-x-neobab/SH.html">LUGAL</w>')]
        #
        self.assertEqual(test_tei_wordXml, comparison_text)






