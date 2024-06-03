from pygr.browser import Browser
from pygr.runner.options import Options
from pygr.item_processor import ItemProcessor
from pygr.definition import Definition
from pygr.common import URL_LIST_TYPE, EXCEL_EXPORT_FORMAT, CSV_EXPORT_FORMAT
from pygr.data import Data
from pygr.item_processor.navigation import Navigation
from pygr.common.logger import Logger


class Runner:
    def __init__(self, definition, exporter=None, db_location=None):
        self.current_data_count = 0
        self.current_url = ""
        self.exporter = exporter
        self.db_location = db_location
        self._def: Definition = definition

    def run_definition(self):
        with Logger(self._def.get("general.package.name", "DEFAULT")) as logger:
            if self._def.get("general.package.type") == "CRAWLER":
                self.run_crawler(logger)
            if self._def.get("general.package.type") == "BROWSER":
                browser = Browser(Options().get(self._def))
                self.run_browser(browser, logger)

    def run_crawler(self, logger):
        return ""

    def run_browser(self, browser, logger):
        logger.log("STARTING JOB")
        logger.log(self.get_job_info_for_log(), separator=True)

        try:
            package_name = self._def.get("general.package.name")
            urls = self.get_urls(logger)

            column_names = self._def.get_column_names(logger)
            logger.log(f"Column names found '{', '.join(column_names)}'", separator=True)

            for i, url in enumerate(urls):
                nav_settings = {"action": "load_url",
                                "url": {"type": "fixed", "value": url, "is_starting": True},
                                "name": "Internal load starting URL"}
                Navigation(Definition(nav_settings), browser, browser.browser).do(logger)

                result = ItemProcessor(self._def.list("items")).process(browser, logger)

                export_format = self._def.get("general.export.format")
                if export_format == EXCEL_EXPORT_FORMAT:
                    Data(package_name, result, column_names).to_excel(f"exports/{package_name}")
                if export_format == CSV_EXPORT_FORMAT:
                    Data(package_name, result, column_names).to_csv(f"exports/{package_name}")

            browser.close_browser()

        except Exception as e:
            browser.close_browser()
            raise e

    def get_urls(self, logger):
        logger.log("Getting URLs to run.")
        try:
            input_type = self._def.get("input_data.type")
            if not input_type:
                raise Exception("No URL input type specified.")

            logger.log(f"URL input type is '{input_type}'.")

            if input_type == URL_LIST_TYPE:
                urls = self._def.list("input_data.value")
                logger.log(f"Found {len(urls)} URLs to run.", separator=True)
                return urls

            logger.warning("No URLs found. Check URL input type or value.")
            return []
        except Exception as e:
            logger.alert(f"Failed getting URLS to run. Error: {e}")
            return []

    def get_job_info_for_log(self):
        return f"JOB SPECS\n- NAME: {self._def.get('general.package.name', 'NO NAME')}\n" \
               f"- TYPE: {self._def.get('general.package.type', 'NO TYPE')}\n" \
               f"- EXPORT: Encoding: {self._def.get('general.export.encoding')} - Format: " \
               f"{self._def.get('general.export.format')}"
