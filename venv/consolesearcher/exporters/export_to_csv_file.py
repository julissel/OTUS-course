# coding: utf-8
import csv
from exporterstrategy import ExporterStrategy


class ExportToCsvFile(ExporterStrategy):

    def export_data(self, sites_dict):

        # Writing to sites.csv
        with open("sites.csv", "w") as sitesfile:
            for site, site_name in sites_dict.items():
                sitesfile.write(f"{site},{site_name}\n")

        print("The result is saved to 'sites.csv'")
