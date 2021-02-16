# coding: utf-8
import requests
from bs4 import BeautifulSoup
from consolesearcher.searcherstrategy import SearcherStrategy


class SearchInGoogle(SearcherStrategy):

    def search_data(self, user_agent, user_query, number_of_results):
        self.sites_dict = dict()
        self.url = f"https://www.google.com/search?q={user_query}&oq={user_query}&num={number_of_results + 2}"

        self.response = requests.get(self.url, headers=user_agent, timeout=20)

        if self.response.status_code != requests.codes.ok:
            print(self.response.status_code)
            print(self.response.raise_for_status())
            return self.sites_dict

        self.soup = BeautifulSoup(self.response.text, "html.parser")
        self.results = self.soup.find_all("div", class_="g")

        for result in self.results:
            self.a_link = result.find("a", href=True)
            self.link_title = result.find("h3")
            self.link = self.a_link["href"]

            if self.link and self.link_title:
                self.sites_dict[self.link] = self.link_title.get_text()

        return self.sites_dict
