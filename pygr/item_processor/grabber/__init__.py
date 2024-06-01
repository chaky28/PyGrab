from pygr.locator import Locator
from pygr.transformer import Transformer
from selenium.webdriver.remote.webelement import WebElement


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


class Grabber:
    def __init__(self, definition, element_to_grab_from):
        self._definition = definition
        self._element_to_grab_from = element_to_grab_from

    def process(self):
        try:
            item_name = self._definition.get("name", "")
            scraped_data = ""

            item = Locator(self._definition.get("locator")).process(self._element_to_grab_from)
            if item is not None:
                attribute = self._definition.get("locator.attribute")
                scraped_data = get_data_from_item(item, attribute)

            transformation = self._definition.get("transformation")
            if transformation is not None:
                scraped_data = Transformer(transformation, scraped_data).do()

            return {item_name: scraped_data.strip()}

        except Exception as e:
            raise e
