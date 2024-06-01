from pygr.common import CLICK_ACTION, LOAD_URL_ACTION
from .click import Click
from .load_url import LoadUrl

class BaseNavigation:
    def __init__(self, definition):
        self._def = definition

    def do(self):
        return self._do_do()

    # ------------------------ Child class methods ------------------------

    def _do_do(self):
        raise Exception("Not implemented.")


class Navigation(BaseNavigation):
    def __init__(self, definition, browser, element):
        super().__init__(definition)
        self._browser = browser
        self._elem = element

    def _do_do(self):
        action = self._def.get("action")
        if action == CLICK_ACTION:
            return Click(self._def, self._elem).do()

        if action == LOAD_URL_ACTION:
            return LoadUrl(self._def, self._browser).do()
