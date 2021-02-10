# coding: utf-8
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from ..searcherstrategy import SearcherStrategy

os.environ["MOZ_HEADLESS"] = "1"
DUCKDUCKGO_CLASS_NAME = "result__a"
HREF_ELEMENT = "href"


class SearchInDuckduckgo(SearcherStrategy):

    def search_data(self, user_agent, user_query, number_of_results):
        self.sites_dict = dict()
        self.url = f"https://duckduckgo.com/?q={user_query}&t=h_&ia=web"

        self.response = requests.get(self.url, headers=user_agent, timeout=20)

        if self.response.status_code == requests.codes.ok:
            self.soup = BeautifulSoup(self.response.text, "html.parser")

            self.result_without_redirection = self.soup.find("a", class_=DUCKDUCKGO_CLASS_NAME)
            if self.result_without_redirection:
                self.results = self.soup.find_all("a", class_=DUCKDUCKGO_CLASS_NAME, limit=number_of_results)

                for result in self.results:
                    self.link = result.get(HREF_ELEMENT)
                    self.link_title = result.get_text()

                    if self.link and self.link_title:
                        self.sites_dict[self.link] = self.link_title

            else:
                '''DuckDuckGo redirected our request to the JavaScript site.
                That is why we are using selenium for this case.'''
                with webdriver.Firefox() as driver:
                    driver.get(self.url)
                    self.results = driver.find_elements_by_name(DUCKDUCKGO_CLASS_NAME)

                    for result in self.results:
                        self.link = result.get_attribute(HREF_ELEMENT)
                        self.link_title = result.text

                        if self.link and self.link_title:
                            self.sites_dict[self.link] = self.link_title

        else:
            print(self.response.status_code)
            print(self.response.raise_for_status())

        return self.sites_dict
