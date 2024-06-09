from pygr.common import REGEX_TR_TYPE
from .regex import regex_transform


class BaseTransformer:
    def __init__(self, transformation, data):
        self._tr = transformation
        self._data = data

    def do(self, logger):
        return self._do_do(logger)

    # ------------------------ Child class methods ------------------------

    def _do_do(self, logger):
        raise Exception("Not implemented.")


class Transformer(BaseTransformer):
    def __init__(self, transformation, data):
        super().__init__(transformation, data)

    def _do_do(self, logger):
        try:
            if not self._tr:
                return self._data

            tr_type = self._tr.get("type")
            if tr_type == REGEX_TR_TYPE:
                return regex_transform(self._data, self._tr)

            logger.warning(f"Transformation type {tr_type} not valid.")
            return ""
        except Exception as e:
            logger.alert(f"Failed transforming data. Error {e}.")
            return ""



