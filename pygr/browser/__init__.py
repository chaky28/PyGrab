from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pygr.common import XPATH_LOCATOR_TYPE, CSS_LOCATOR_TYPE


def get_by_locator_value(locator_type):
    if locator_type == XPATH_LOCATOR_TYPE:
        return By.XPATH
    if locator_type == CSS_LOCATOR_TYPE:
        return By.CSS_SELECTOR
    return By.XPATH


class Browser:
    def __init__(self, driver_options):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                        options=driver_options)
        self.starting_url = ""
        self._browser_status = 'Loaded'

    def update_browser_status(self, status):
        self._browser_status = status

    def load_url(self, url: str, save_as_starting=False):
        try:
            self.update_browser_status("Loading")
            self.browser.get(url)
            self.update_browser_status("Loaded")

            if save_as_starting:
                self.starting_url = url

        except Exception as e:
            self.update_browser_status("Error")
            raise e

    def close_browser(self):
        self.browser.close()

    def get_html(self):
        return self.browser.page_source

    def get_loaded_url(self):
        return self.browser.current_url

