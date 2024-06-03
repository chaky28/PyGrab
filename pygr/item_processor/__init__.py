from . import grabber
from . import grabber_list
from . import pagination
from . import navigation
from . import grabber_internal
from pygr.common import GRABBER_TYPE, GRABBER_LIST_TYPE, PAGINATION_TYPE, NAVIGATION_TYPE, GRABBER_INTERNAL_TYPE


class ItemProcessor:
    def __init__(self, items):
        self._items = items

    def process(self, browser, logger):
        result = {}
        self.get_item_list_data(browser, "main-0", result, logger)
        return result

    def get_item_list_data(self, browser, parent_name, result, logger, element=None, items=None):
        if not element:
            element = browser.browser
        if not items:
            items = self._items

        if not result.get(parent_name):
            result[parent_name] = []
        does_grabber_list_exists = False

        for item in items:
            item_type = item.get("type")
            if item_type == GRABBER_TYPE:
                grabber_obj = grabber.Grabber(item, element)
                result.get(parent_name).append(grabber_obj.process())

            if item_type == GRABBER_LIST_TYPE:
                grabber_list_obj = grabber_list.GrabberList(item, parent_name)
                if grabber_list_obj.has_elements(element):
                    does_grabber_list_exists = True
                    grabber_list_obj.process(browser, element, result, logger)

            if item_type == PAGINATION_TYPE:
                pagination_obj = pagination.Pagination(item, parent_name, self._items)
                pagination_obj.process(browser, element, result, logger)

            if item_type == NAVIGATION_TYPE:
                navigation_obj = navigation.Navigation(item, browser, element)
                navigation_obj.do(logger)

            if item_type == GRABBER_INTERNAL_TYPE:
                grabber_internal_obj = grabber_internal.GrabberInternal(item, browser)
                result.get(parent_name).append(grabber_internal_obj.process())

        if not does_grabber_list_exists:
            result[f"{parent_name}#EXPORT"] = result.get(parent_name)
            del result[parent_name]
