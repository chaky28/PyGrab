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
    def __init__(self, pacakge_name, data, column_names, logger):
        super().__init__(data)
        self._package_name = pacakge_name
        self._column_names = column_names
        self.logger = logger

    def _do_normalize_data(self):
        self.logger.log(f"Normalizing data for export.")
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
        try:
            self.logger.log("Generating CSV...")

            data = self._do_normalize_data()
            df = pd.DataFrame(columns=self._column_names, data=data)

            make_directory(path)
            full_path = os.path.join(path, f'{self._package_name}_{get_timestamp()}.csv')

            df.to_csv(f"{full_path}", index=False,
                      encoding=encoding)

            self.logger.log(f"Successfully generated CSV in location {full_path}", separator=True)
        except Exception as e:
            self.logger.alert(f"Failed to generate CSV. Error {e}.", separator=True)

    def _do_to_excel(self, path, encoding):
        try:
            self.logger.log("Generating EXCEL...")

            data = self._do_normalize_data()
            df = pd.DataFrame(columns=self._column_names, data=data)

            make_directory(path)
            full_path = os.path.join(path, f'{self._package_name}_{get_timestamp()}.xlsx')

            df.to_excel(f"{full_path}", index=False)

            self.logger.log("Successfully generated EXCEL.", separator=True)
        except Exception as e:
            self.logger.alert(f"Failed to generate EXCEL. Error {e}.", separator=True)


