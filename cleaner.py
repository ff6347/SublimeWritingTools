import re
import sublime
from bs4 import BeautifulSoup
from markdown import markdown

class Cleaner(object):

    def plain_text(self, mdown):
        html = markdown(mdown)
        text = BeautifulSoup(html, "html.parser").text
        return text

    def lower_case(self, txt):
        return txt.lower()

    def hypens(self, txt):
        return re.sub(r"\ ","-", txt)

    def strip(self, txt):
        return txt.strip()

    def punctuation(self, txt):
        # https://stackoverflow.com/a/21209161/1770432
        pattern = r"\W(?<!-|_|\s)"
        return re.sub(pattern, "", txt)

    def leading_numbers(self, txt):
        pattern = r"^\d"
        return re.sub(pattern, "", txt)
