from pygr.browser import Browser
from pygr.runner.options import Options
from pygr.item_processor import ItemProcessor
from pygr.definition import Definition
from pygr.common import URL_LIST_TYPE
from pygr.data import Data
from pygr.navigations.load_url import LoadUrl


class Runner:
    def __init__(self, definition, exporter=None, db_location=None):
        self.current_data_count = 0
        self.current_url = ""
        self.exporter = exporter
        self.db_location = db_location
        self._def: Definition = definition

    def run_definition(self):
        if self._def.get("general.package.type") == "CRAWLER":
            self.run_crawler()
        if self._def.get("general.package.type") == "BROWSER":
            browser = Browser(Options().get(self._def))
            self.run_browser(browser)

    def run_crawler(self):
        return ""

    def run_browser(self, browser):
        try:
            package_name = self._def.get("general.package.name")
            urls = self.get_urls()
            column_names = self._def.get_column_names()

            for i, url in enumerate(urls):
                LoadUrl({"nav_type": "fixed_url", "url": url}, browser).do()

                result = ItemProcessor(self._def.list("items")).process(browser)

                Data(package_name, result, column_names).to_csv(f"exports/{package_name}", create_dir=True)

            browser.close_browser()

        except Exception as e:
            browser.close_browser()
            raise e

    def get_urls(self):
        input_type = self._def.get("input_data.type")
        if input_type == URL_LIST_TYPE:
            return self._def.list("input_data.value")
        return []



