from benedict import benedict
from pygr.common import GRABBER_TYPE, GRABBER_LIST_TYPE, ITEMS_THAT_EXPORT


class BaseDefinition:
    def __init__(self, definition):
        super().__init__()
        self._def = benedict(definition, format="json")

    def get(self, path, default=None):
        return self._do_get(path, default)

    def list(self, path):
        return self._do_list(path)

    def get_column_names(self):
        return self._do_get_colum_names()

    # ------------------------ Child class methods ------------------------

    def _do_get(self, path, default):
        raise Exception("Not implemented.")

    def _do_list(self, path):
        raise Exception("Not implemented.")

    def _do_get_colum_names(self):
        raise Exception("Not implemented.")


class Definition(BaseDefinition):
    def __init__(self, definition):
        super().__init__(definition)

    def _do_get(self, path, default):
        return self._def.get(path, default)

    def _do_list(self, path):
        return self._def.get_list(path)

    def _do_get_colum_names(self, items=None):
        if not items:
            items = self._def.get_list("items")

        result = []
        for item in items:
            item_name = item.get("name")
            item_type = item.get("type")
            if item_type in ITEMS_THAT_EXPORT and item_name not in result:
                result.append(item_name)

            if item_type == GRABBER_LIST_TYPE:
                result = result + self._do_get_colum_names(item.get_list("items"))

        return result
