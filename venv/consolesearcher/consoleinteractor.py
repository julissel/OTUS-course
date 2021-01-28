# coding: utf-8


class ConsoleInteractor():

    DEFAULT_QUERY = 'PYTHON'
    DEFAULT_SEARCH_ENGINE = '1'  # Google.com
    DEFAULT_NUMBER_OF_RESULTS = 1
    DEFAULT_OUTPUT_FORMAT = '1'  # console

    def __init__(self):
        self.user_query = self.DEFAULT_QUERY
        self.search_engine = self.DEFAULT_SEARCH_ENGINE
        self.number_of_results = self.DEFAULT_NUMBER_OF_RESULTS
        self.output_format = self.DEFAULT_OUTPUT_FORMAT

    def get_user_query(self):
        console_user_query = input("Enter your request: ")
        if len(console_user_query) > 0:
            self.user_query = console_user_query

    def get_search_engine(self):
        console_search_engine = input("Select a search engine (1 - google.com, 2 - duckduckgo.com): ")
        if console_search_engine in ('1', '2'):
            self.search_engine = console_search_engine

    def get_number_of_results(self):
        console_number_of_results = input("Number of results: ")
        try:
            self.number_of_results = abs(int(console_number_of_results))
        except:
            pass

    def get_output_format(self):
        console_output_format = input("Specify the output format (1 - console, 2 - json, 3 - xml, 4 - csv): ")
        if console_output_format in ('1', '2', '3', '4'):
            self.output_format = console_output_format

    def processing_user_input(self):
        self.get_user_query()
        self.get_search_engine()
        self.get_number_of_results()
        self.get_output_format()

