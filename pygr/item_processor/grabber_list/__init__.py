from pygr.locator import Locator
from pygr.definition import Definition
from ... import item_processor as it_pr


class GrabberList:
    def __init__(self, definition: Definition, parent_name):
        self._def = definition
        self._parent_name = parent_name

    def has_elements(self, element):
        elements = Locator(self._def.get("locator")).process(element, find_all=True)
        return len(elements) != 0

    def process(self, browser, element, result, logger):
        try:
            elements = Locator(self._def.get("locator")).process(element, find_all=True)
            if len(elements) != 0:
                for i, l_elem in enumerate(elements):
                    items = self._def.get("items")
                    name = self._def.get("name")
                    it_pr.ItemProcessor(items).get_item_list_data(browser, f'{self._parent_name}_{name}-{i}', result,
                                                                  logger, l_elem)
        except Exception as e:
            raise e
