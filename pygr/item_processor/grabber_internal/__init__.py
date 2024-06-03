from datetime import datetime as dt
from pygr.common import INTERNAL_LOADED_URL_LOCATOR_TYPE, INTERNAL_STARTING_URL_LOCATOR_TYPE, \
    INTERNAL_DATETIME_URL_LOCATOR_TYPE, DEFAULT_DATETIME_FORMAT
from pygr.browser import Browser
from pygr.transformer import Transformer


def get_data_from_item(item, attribute):
    try:
        if attribute is not None:
            if attribute == "innerText":
                return item.get_property("innerText").strip()
            if attribute == "textContent" or attribute is None:
                return item.get_property("textContent").strip()
            return item.get_attribute(attribute).strip()
        return item.get_property("textContent").strip()
    except Exception as e:
        print(type(e))
        return ""


class GrabberInternal:
    def __init__(self, definition, browser: Browser):
        self._def = definition
        self._browser = browser

    def process(self):
        try:
            name = self._def.get("name")
            value = ""
            locator_type = self._def.get("locator.type")
            if locator_type == INTERNAL_LOADED_URL_LOCATOR_TYPE:
                value = self._browser.get_loaded_url().strip()

            if locator_type == INTERNAL_STARTING_URL_LOCATOR_TYPE:
                value = self._browser.starting_url.strip()

            if locator_type == INTERNAL_DATETIME_URL_LOCATOR_TYPE:
                date_format = self._def.get("format", DEFAULT_DATETIME_FORMAT)
                value = dt.now().strftime(date_format)

            value = Transformer(self._def.get("transformation"), value).do()
            return {name: value}

        except Exception as e:
            return ""
