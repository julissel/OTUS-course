# coding: utf-8
import requests
from bs4 import BeautifulSoup
from searcherstrategy import SearcherStrategy


class SearchInDuckduckgo(SearcherStrategy):

    def search_data(self, user_agent, user_query, number_of_results):

        self.url = f"https://duckduckgo.com/?q={user_query}&t=h_&ia=web"

        self.response = requests.get(self.url, headers=user_agent, timeout=20)
        self.response.raise_for_status()

        self.soup = BeautifulSoup(self.response.text, "html.parser")
        self.results = self.soup.find_all("a", class_="result__a", limit=number_of_results)

        self.sites_dict = dict()
        for result in self.results:
            self.link = result.get("href")
            self.link_title = result.get_text()

            if self.link and self.link_title:
                self.sites_dict[self.link] = self.link_title

        return self.sites_dict
