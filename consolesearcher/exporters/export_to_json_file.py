# coding: utf-8
import json
from exporterstrategy import ExporterStrategy


class ExportToJsonFile(ExporterStrategy):

    def export_data(self, sites_dict):

        # Serializing in json
        json_obj = json.dumps(sites_dict, indent=4)

        # Writing to sites.json
        with open("sites.json", "w") as sitesfile:
            sitesfile.write(json_obj)

        print("The result is saved to 'sites.json'")
