# coding: utf-8
import json
from consolesearcher.exporterstrategy import ExporterStrategy


class ExportToJsonFile(ExporterStrategy):

    def export_data(self, sites_dict):

        # Serializing in json
        json_obj = json.dumps(sites_dict, indent=4,  ensure_ascii=False)

        # Writing to sites.json
        with open("sites.json", "w", encoding='utf8') as sitesfile:
            sitesfile.write(json_obj)

        print("The result is saved to 'sites.json'")
