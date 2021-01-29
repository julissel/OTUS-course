# coding: utf-8
import exporterstrategy
import searcherstrategy
from consoleinteractor import ConsoleInteractor
from exporters.export_to_console import ExportToConsole
from exporters.export_to_json_file import ExportToJsonFile
from exporters.export_to_xml_file import ExportToXmlFile
from exporters.export_to_csv_file import ExportToCsvFile
from searchers.search_in_duckduckgo import SearchInDuckduckgo
from searchers.search_in_google import SearchInGoogle


DEFAULT_USER_AGENT = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0'}

def main():
    interactor = ConsoleInteractor()
    interactor.processing_user_input()
    user_query = interactor.user_query
    search_engine = interactor.search_engine
    number_of_results = interactor.number_of_results
    output_format = interactor.output_format

    searcher = {
        "1": SearchInGoogle(),
        "2": SearchInDuckduckgo()
    }

    sites_dict = searcher.get(search_engine).search_data(DEFAULT_USER_AGENT, user_query, number_of_results)

    exporter = {
        "1": ExportToConsole(),
        "2": ExportToJsonFile(),
        "3": ExportToXmlFile(),
        "4": ExportToCsvFile()
    }

    exported_sites = exporter.get(output_format).export_data(sites_dict)


if __name__ == '__main__':
    main()
