from pygr.browser import get_by_locator_value
from selenium.webdriver import Chrome


class Locator:

    def __init__(self, definition):
        self.locator_type = definition.get("type")
        self.locator_value = definition.get("value")

    def process(self, element, find_all=False):
        try:
            by_value = get_by_locator_value(self.locator_type)
            selection = element.find_elements(by=by_value, value=self.locator_value)
            if find_all:
                if not selection:
                    return []
                return selection

            if not selection:
                return None

            return selection[0]
        except Exception as e:
            if find_all:
                return []
            return None
