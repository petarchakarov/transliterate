# -*- coding: utf-8 -*-

__title__ = 'transliterate.contrib.languages.he.translit_language_pack'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('HebrewLanguagePack',)

from transliterate.base import TranslitLanguagePack, registry

class HebrewLanguagePack(TranslitLanguagePack):
    """
    Language pack for Hebrew language. See http://en.wikipedia.org/wiki/Hebrew_alphabet for details. See
    the http://en.wikipedia.org/wiki/Romanization_of_Hebrew#When_to_transliterate for transliteration details.
    Note, that this language pack implements the new standares (2006) of Hebrew Academy.

    Confirmed
        a אּ
        v ב
        b בּּּ
        ּg ג
        gg ג
        ּd ד
        dd דּ
        h ה
        h הּ
        v ו
        vv וּ
        z ז
        zz זּ
        
    """
    language_code = "he"
    language_name = "Hebrew"
    character_ranges = ((0x0530, 0x058F), (0xFB10, 0xFB1F))
    mapping = (
        "abgdvzhilmnsfckrt",
        # trkcfsnmlihzvdgbа
        "אבגדוזחילמנספצקרת",
    )
    reversed_specific_mapping = (
        "פ",
        # p
        "p"
    )
    pre_processor_mapping = {
        # lowercase
        "ha'": "ה",
        "tt": "ט",
        "ka": "כ",
        "aa": "ע",
        "sh": "ש",
        "fs": "ף",
        "cs": "ץ",
        "ms": "ם",
        "ns": "ן",
        "ks": "ך",
    }
    detectable = True


#registry.register(HebrewLanguagePack)
