import jieba
from hanziconv import HanziConv as hanzC

import pinyin
from pinyin import cedict

import hanzidentifier as hanzI

import sys

from .exceptions import ChineseCharsNotFound
import json

class Translator:
    """
    Class used to translate inputted text containing Chinese characters into simplified and traditional Chinese, while acquiring the pinyin and definitions
    of each segment found in the text.

    Args:
        text_input (str): A string, containing Chinese characters.

    Attributes:
        text_input (str): Stored text_input.
        seglist_sim (:obj:`list` of :obj:`str`): A list containing segmented simplified Chinese characters produced by method 'segment_text'
        seglist_trad (:obj:`list` of :obj:`str`): A list containing segmented traditional Chinese characters produced by method 'segment_text'
        list_py (:obj:`list` of :obj:`str`): A list containing pinyin for each character in the segmented lists, produced by method 'romanize_text'
        list_def (:obj:`list` of :obj:`str`): A list containing definitions for each segment found in the segmented lists, 
            produced by method 'acquire_definition'

    """
    def __init__(self, text_input):
        try:
            self.text_input = self.check_text(text_input)
            self.list_sim = []
            self.list_trad = []
            self.list_py = []
            self.list_def = []
            self.segment_text()
            self.romanize_text()
            self.acquire_definition()
        except ChineseCharsNotFound as e:
            print(e.msg)

    @staticmethod
    def check_text(text_input):
        """
        Checks to see if the input has Chinese characters, and whether or not it is in simplified or traditional. Returns text_input if
        it does, raises an error if none are found.

        Args:
            text_input (str): A string, containing Chinese characters.

        Returns:
            text_input (str): Original string.
        
        Raises:
            ChineseCharsNotFound: When no chinese characters are found in text_input.
        """

        char_type = hanzI.identify(text_input)
        if char_type == 0:
            raise ChineseCharsNotFound(text_input)
        else:
            return text_input


    def simplify_text(self):
        """
        Simplifies text input into simplified Chinese characters in preparation for segmentation. For reasons why
        simplification is done first, check documentation for method 'segment_text'.

        Returns:
            text_sim (str): A string containing simplified Chinese characters, obtained by simplifying text_input using hanziconverter.
        """

        text_sim = hanzC.toSimplified(self.text_input)
        
        return text_sim
        
    def segment_text(self):
        """
        Simplifies text input first, and then segments it using the jieba module. Simplification is done first since 
        jieba was made to work with simplified Chinese.
        """

        text_sim = self.simplify_text()

        self.list_sim = list(jieba.cut(text_sim))
        self.list_trad = list(map(hanzC.toTraditional, self.list_sim))

    def romanize_text(self):
        """
        Gets the pinyin for the segmented Chinese characters.
        """
        for char in self.list_sim:
            self.list_py.append(pinyin.get(char))

    def acquire_definition(self):
        """
        Gets lists of definitions for the segmented Chinese characters.
        """
        for char in self.list_sim:
            self.list_def.append(cedict.translate_word(char))
    
    def jsonify_attributes(self):
        """
        """
        json_file = {
            'input': self.text_input,
            'sim': self.list_sim,
            'trad': self.list_trad,
            'py': self.list_py,
            'def': self.list_def
                }
        return json.dumps(json_file)

if __name__== "__main__":
    app = Translator("我来到北京清华大学")