from pygr.browser import Browser
from pygr.item_processor.grabber import Grabber


class BaseLoadUrl:
    def __init__(self, definition):
        self._def = definition

    def do(self, logger):
        self._do_do(logger)

    # ------------------------ Child class methods ------------------------

    def _do_do(self, logger):
        raise Exception("Not implemented.")


class LoadUrl(BaseLoadUrl):
    def __init__(self, definition, browser: Browser):
        super().__init__(definition)
        self._browser = browser

    def _do_do(self, logger):
        url_type = self._def.get("url.type")
        logger.log(f"Executing load url of type {url_type}.")
        if url_type == "fixed":
            return self._manage_fixed_load_url(logger)
        if url_type == "dynamic":
            return self._manage_dynamic_load_url(logger)

    def _manage_dynamic_load_url(self, logger):
        url = Grabber(self._def.get("url.value"), self._browser.browser).process()
        if url == "":
            logger.warn("No URL found to load.")
            return False

        self._browser.load_url(url, logger, save_as_starting=self._def.get("url.is_starting"))
        return True

    def _manage_fixed_load_url(self, logger):
        url = self._def.get("url.value")
        self._browser.load_url(url, logger, save_as_starting=self._def.get("url.is_starting"))
        return True

