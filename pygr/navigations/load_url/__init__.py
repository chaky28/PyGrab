from pygr.browser import Browser
from pygr.item_processor.grabber import Grabber


class BaseLoadUrl:
    def __init__(self, definition):
        self._def = definition

    def do(self):
        self._do_do()

    # ------------------------ Child class methods ------------------------

    def _do_do(self):
        raise Exception("Not implemented.")


class LoadUrl(BaseLoadUrl):
    def __init__(self, definition, browser: Browser):
        super().__init__(definition)
        self._browser = browser

    def _do_do(self):
        nav_type = self._def.get("nav_type")
        if nav_type == "fixed_url":
            self._manage_fixed_load_url()
        if nav_type == "url":
            self._manage_load_url()

    def _manage_load_url(self):
        url = Grabber(self._def, self._browser.browser).process()
        self._browser.load_url(url)

    def _manage_fixed_load_url(self):
        self._browser.load_url(self._def.get("url"))

