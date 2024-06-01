from pygr.browser import Browser
from pygr.runner.options import Options
from pygr.item_processor import ItemProcessor
from pygr.definition import Definition
from pygr.common import URL_LIST_TYPE, EXCEL_EXPORT_FORMAT, CSV_EXPORT_FORMAT
from pygr.data import Data
from pygr.item_processor.navigation import Navigation


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

                Navigation(Definition({"action": "load_url", "url": {"type": "fixed", "value": url,
                                                                     "is_starting": True}}),
                           browser, browser.browser).do()

                result = ItemProcessor(self._def.list("items")).process(browser)

                export_format = self._def.get("general.export.format")
                if export_format == EXCEL_EXPORT_FORMAT:
                    Data(package_name, result, column_names).to_excel(f"exports/{package_name}")
                if export_format == CSV_EXPORT_FORMAT:
                    Data(package_name, result, column_names).to_csv(f"exports/{package_name}")

            browser.close_browser()

        except Exception as e:
            browser.close_browser()
            raise e

    def get_urls(self):
        input_type = self._def.get("input_data.type")
        if input_type == URL_LIST_TYPE:
            return self._def.list("input_data.value")
        return []



