import pandas as pd

class SP500Scrapper:
    def __init__(self):
        self._data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

    def get_string(self):
        result = "symbols = [\n"
        for row in self._data[0].iterrows():
            result += ("    '" + row[1][0] + "', # " + row[1][1] + "\n")
        result += "]"
        return result

    def get_list(self):
        return self._data[0]['Symbol'].tolist()
