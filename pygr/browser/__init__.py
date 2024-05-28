from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def get_by_locator_value(locator_type):
    if locator_type == "XPATH":
        return By.XPATH
    if locator_type == "CSS":
        return By.CSS_SELECTOR
    return By.XPATH


class Browser:
    def __init__(self, driver_options):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                        options=driver_options)
        self.browser_status = 'Loaded'

    def update_browser_status(self, status):
        self.browser_status = status

    def load_url(self, url: str):
        try:
            self.update_browser_status("Loading")
            self.browser.get(url)
            self.update_browser_status("Loaded")
        except Exception as e:
            self.update_browser_status("Error")
            raise e

    def close_browser(self):
        self.browser.close()

    def get_html(self):
        return self.browser.page_source

