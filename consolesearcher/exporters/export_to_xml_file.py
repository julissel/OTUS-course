# coding: utf-8
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
from consolesearcher.exporterstrategy import ExporterStrategy


class ExportToXmlFile(ExporterStrategy):

    def export_data(self, sites_dict):

        # Serializing in xml
        xml_obj = dicttoxml(sites_dict, attr_type=False)
        pretty_xml_obj = parseString(xml_obj).toprettyxml()

        # Writing to sites.xml
        with open("sites.xml", "w") as sitesfile:
            sitesfile.write(pretty_xml_obj)

        print("The result is saved to 'sites.xml'")
