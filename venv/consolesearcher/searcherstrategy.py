# coding: utf-8
from abc import ABC, abstractmethod


class SearcherStrategy(ABC):

    @abstractmethod
    def search_data(self, user_agent, user_query, number_of_results):
        pass
