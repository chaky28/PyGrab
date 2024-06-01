import pathlib
import os
import pandas as pd
import datetime as dt
from pygr.common import DEFAULT_EXPORT_ENCODING


def get_timestamp():
    now = dt.datetime.now().strftime("%H%M%S%f")
    return now


def make_directory(rel_path):
    abs_path = os.path.join(os.path.abspath("."), rel_path)
    pathlib.Path(abs_path).mkdir(parents=True, exist_ok=True)


class BaseData:
    def __init__(self, data):
        self._data = data

    def to_csv(self, path, encoding=DEFAULT_EXPORT_ENCODING):
        self._do_to_csv(path, encoding)

    def to_excel(self, path, encoding=DEFAULT_EXPORT_ENCODING):
        self._do_to_excel(path, encoding)

    # ------------------------ Child class methods ------------------------

    def _do_to_csv(self, path, encoding):
        raise Exception("Not implemented.")

    def _do_to_excel(self, path, encoding):
        raise Exception("Not implemented.")


class Data(BaseData):
    def __init__(self, pacakge_name, data, column_names):
        super().__init__(data)
        self._package_name = pacakge_name
        self._column_names = column_names

    def _do_normalize_data(self):
        result = []
        for key, value in self._data.items():
            if "#EXPORT" in key:
                export_result = {}
                path = key.split("_")
                for i in range(len(path)):
                    iterator = 0
                    sub_path = ""
                    while iterator <= i:
                        sub_path += path[iterator]
                        if iterator < i:
                            sub_path += "_"
                        iterator += 1
                    for column in self._data[sub_path]:
                        export_result = {**export_result, **column}
                result.append(export_result)
        return result

    def _do_to_csv(self, path, encoding):
        data = self._do_normalize_data()
        df = pd.DataFrame(columns=self._column_names, data=data)

        make_directory(path)

        df.to_csv(f"{os.path.join(path, f'{self._package_name}_{get_timestamp()}.csv')}", index=False,
                  encoding=encoding)

    def _do_to_excel(self, path, encoding):
        data = self._do_normalize_data()
        df = pd.DataFrame(columns=self._column_names, data=data)

        make_directory(path)

        df.to_excel(f"{os.path.join(path, f'{self._package_name}_{get_timestamp()}.xlsx')}", index=False)


