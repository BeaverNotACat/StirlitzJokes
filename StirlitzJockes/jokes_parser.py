import requests
from requests import Response
from bs4 import BeautifulSoup as bs
from bs4 import ResultSet
import random


class JokesParser():
    def __init__(self, link: str) -> None:
        self.link = link

    @staticmethod
    def __randomize_link_ending() -> str:
        return random.choice('1234')

    @classmethod
    def __choose_joke_from_set(self, rset: ResultSet) -> str:
        return random.choice(rset).text

    @classmethod
    def __send_get_request(self, link: str) -> str:
        return requests.get(link).text

    @classmethod
    def __parse_jokes_text(self, page_html: str) -> ResultSet:
        bsoup = bs(page_html, "html.parser")
        return bsoup.find_all('div', class_='text')

    def get_joke(self):
        link = self.link+self.__randomize_link_ending()
        page_html = self.__send_get_request(link)
        rset = self.__parse_jokes_text(page_html)
        return self.__choose_joke_from_set(rset)
