from pygr.browser import Browser
from pygr.locator import Locator


class BaseClick:
    def __init__(self, definition):
        self._def = definition

    def do(self, logger):
        return self._do_do(logger)

    # ------------------------ Child class methods ------------------------

    def _do_do(self, logger):
        raise Exception("Not implemented.")


class Click(BaseClick):
    def __init__(self, definition, element):
        super().__init__(definition)
        self._element = element

    def _do_do(self, logger):
        try:
            element = Locator(self._def.get("locator")).process(self._element)
            if not element:
                logger.warning("No element found to click on.")
                return False

            element.click()
            logger.log("Successfully clicked on element.")
            return True
        except Exception as e:
            logger.alert(f"Failed trying to click on element. Error {e}")
            return False


