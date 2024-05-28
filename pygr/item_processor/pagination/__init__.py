from ... import item_processor as it_pr
from pygr.locator import Locator
from pygr.navigations.click import Click


class Pagination:
    def __init__(self, definition, parent_name, items):
        self._def = definition
        self._parent_name = parent_name
        self._items = items

    def get_grabber_list_to_repeat(self, items=None):
        if not items:
            items = self._items

        grabber_list = self._def.get("repeat_grabber_list")
        for item in items:
            if item.get("name") == grabber_list:
                return item
            else:
                if item.get("type") == "grabber_list":
                    return self.get_grabber_list_to_repeat(item.get("items", []))

    def paginate(self, browser, element):
        pag_type = self._def.get("action")

        if self._def.get("action") == "click":
            return Click(self._def, element).do()

        return False

    def process(self, browser, element, result):
        try:
            pagination_count = 0
            grabber_list = self.get_grabber_list_to_repeat()

            while self.paginate(browser, element):

                pagination_name = self._def.get("name")
                parent_name = f"{self._parent_name}_{pagination_name}{pagination_count}"
                it_pr.ItemProcessor([grabber_list]).get_item_list_data(browser, parent_name, result)

                pagination_count += 1
        except Exception as e:
            raise e
