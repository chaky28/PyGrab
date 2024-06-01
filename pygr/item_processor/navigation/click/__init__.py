from pygr.browser import Browser
from pygr.locator import Locator


class BaseClick:
    def __init__(self, definition):
        self._def = definition

    def do(self):
        return self._do_do()

    # ------------------------ Child class methods ------------------------

    def _do_do(self):
        raise Exception("Not implemented.")


class Click(BaseClick):
    def __init__(self, definition, element):
        super().__init__(definition)
        self._element = element

    def _do_do(self):
        try:
            element = Locator(self._def.get("locator")).process(self._element)
            if not element:
                return False

            element.click()
            return True
        except Exception as e:
            return False


