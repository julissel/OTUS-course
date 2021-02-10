# coding: utf-8
from consolesearcher.exporterstrategy import ExporterStrategy


class ExportToConsole(ExporterStrategy):

    def export_data(self, sites_dict):
        print("Result:")
        for site, site_name in sites_dict.items():
            print(f"Link = {site},  Site name = {site_name}")
