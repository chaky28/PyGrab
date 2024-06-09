from pygr.locator import Locator
from pygr.transformer import Transformer
from pygr.common import DEFAULT_ITEM_NAME


def get_data_from_item(item, attribute, logger):
    try:
        if attribute is not None:
            if attribute == "innerText":
                return item.get_property("innerText").strip()
            if attribute == "textContent" or attribute is None:
                return item.get_property("textContent").strip()
            return item.get_attribute(attribute).strip()
        return item.get_property("textContent").strip()
    except Exception as e:
        logger.alert(f"Failed getting data from web element. Error {e}.")
        return ""


class Grabber:
    def __init__(self, definition, element_to_grab_from):
        self._definition = definition
        self._element_to_grab_from = element_to_grab_from

    def process(self, logger):
        item_name = self._definition.get("name", DEFAULT_ITEM_NAME)
        try:
            scraped_data = ""

            item = Locator(self._definition.get("locator")).process(self._element_to_grab_from, logger)
            if item is not None:
                attribute = self._definition.get("locator.attribute")
                scraped_data = get_data_from_item(item, attribute, logger)

            transformation = self._definition.get("transformation")
            if transformation is not None:
                scraped_data = Transformer(transformation, scraped_data).do(logger)

            if scraped_data == "":
                logger.warning(f"No data was produced for item '{item_name}'.")

            return {item_name: scraped_data.strip()}

        except Exception as e:
            logger.alert(f"Failed grabbing data. Item {item_name}. Error {e}.")
            return {item_name: ""}
