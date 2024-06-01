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
        url_type = self._def.get("url.type")
        url = ""
        if url_type == "fixed":
            url = self._manage_fixed_load_url()
        if url_type == "dynamic":
            url = self._manage_dynamic_load_url()

    def _manage_dynamic_load_url(self):
        url = Grabber(self._def.get("url.value"), self._browser.browser).process()
        if url == "":
            return False

        self._browser.load_url(url, save_as_starting=self._def.get("url.is_starting"))
        return True

    def _manage_fixed_load_url(self):
        url = self._def.get("url.value")
        self._browser.load_url(url, save_as_starting=self._def.get("url.is_starting"))
        return True

