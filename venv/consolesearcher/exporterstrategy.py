# coding: utf-8
from abc import ABC, abstractmethod


class ExporterStrategy(ABC):

    @abstractmethod
    def export_data(self, sites_dict):
        pass
