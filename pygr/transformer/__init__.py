from pygr.common import REGEX_TR_TYPE
from .regex import regex_transform


class BaseTransformer:
    def __init__(self, transformation, data):
        self._tr = transformation
        self._data = data

    def do(self, logger, only_get_first):
        return self._do_do(logger, only_get_first)

    # ------------------------ Child class methods ------------------------

    def _do_do(self, logger, only_get_first):
        raise Exception("Not implemented.")


class Transformer(BaseTransformer):
    def __init__(self, transformation, data):
        super().__init__(transformation, data)

    def _do_do(self, logger, only_get_first=True):
        try:
            if not self._tr:
                return self._data

            if not isinstance(self._data, list) and not isinstance(self._data, str):
                raise Exception("Data type not supported.")

            if isinstance(self._data, list) and len(self._data) == 0:
                raise Exception("No data passed to transform.")

            if isinstance(self._data, str):
                return regex_transform(self._data, self._tr)

            tr_type = self._tr.get("type")
            if tr_type == REGEX_TR_TYPE:
                if only_get_first:
                    return regex_transform(self._data[0], self._tr)

                result = []
                for data in self._data:
                    result.append(regex_transform(data, self._tr))
                return result

            logger.warning(f"Transformation type {tr_type} not valid.")
            return ""
        except Exception as e:
            logger.alert(f"Failed transforming data. Error {e}.")
            return ""



