from . import LOGS_FILE_PATH, DEFAULT_DATETIME_FORMAT, LOG_SEPARATOR
import pathlib
import os
from datetime import datetime as dt
from pygr.data import get_timestamp


class BaseLogger:
    def __init__(self, package_name, rel_filepath, datetime_format, full_filepath):
        self._name = package_name
        self._full_filepath = full_filepath
        self._filepath = self._initialize_logger_filepath(rel_filepath, full_filepath)
        self._dt_format = datetime_format

    def __enter__(self):
        self._file = self._initialize_logger_file()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._do_exit()
        return True

    def _initialize_logger_file(self):
        return self._do_initialize_logger_file()

    def _initialize_logger_filepath(self, rel_file_path, full_filepath):
        return self._do_initialize_logger_filepath(rel_file_path, full_filepath)

    def log(self, text, separator=False):
        self._do_log(text, separator)

    def alert(self, text, separator=False):
        self._do_alert(text, separator)

    def warning(self, text, separator=False):
        self._do_warning(text, separator)

    def debug(self, text, separator=False):
        self._do_debug(text, separator)

    # ------------------------ Child class methods ------------------------

    def _do_initialize_logger_file(self):
        raise Exception("Not implemented.")

    def _do_initialize_logger_filepath(self, rel_file_path, full_filepath):
        raise Exception("Not implemented.")

    def _do_log(self, text, separator):
        raise Exception("Not implemented.")

    def _do_alert(self, text, separator):
        raise Exception("Not implemented.")

    def _do_warning(self, text, separator):
        raise Exception("Not implemented.")

    def _do_debug(self, text, separator):
        raise Exception("Not implemented.")

    def _do_exit(self):
        raise Exception("Not implemented.")


class Logger(BaseLogger):
    def __init__(self, package_name, logs_file_path=LOGS_FILE_PATH, datetime_format=DEFAULT_DATETIME_FORMAT,
                 full_filepath=None):
        super().__init__(package_name, logs_file_path, datetime_format, full_filepath)

    def _do_exit(self):
        try:
            if not self._file:
                print(f"WARN: No log file to close in filepath {self._filepath}.")
                return

            self._file.close()
            print(f"INFO: Log file in {self._filepath} was closed.")

        except Exception as e:
            print(f"ALERT: Failed closing log file in path {self._filepath}. Error {e}")

    def _do_initialize_logger_filepath(self, rel_file_path, full_filepath):
        if full_filepath is not None:
            return full_filepath

        path = os.path.join(os.path.abspath("."), f"{rel_file_path}/{self._name}")
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)
        return path

    def _do_initialize_logger_file(self):
        if self._full_filepath is not None:
            return open(self._full_filepath, "a", encoding="UTF8")

        self._filepath = f"{self._filepath}/log_{get_timestamp()}.txt"
        return open(self._filepath, "a",  encoding="UTF8")

    def get_filepath(self):
        return self._filepath

    def _do_log(self, text, separator):
        text = f"{dt.now().strftime(self._dt_format)} - INFO : {text}"
        if separator:
            text += f"\n{LOG_SEPARATOR}"
        text += f"\n"
        self._file.write(text)

    def _do_warning(self, text, separator):
        text = f"{dt.now().strftime(self._dt_format)} - WARN : {text}"
        if separator:
            text += f"\n{LOG_SEPARATOR}"
        text += f"\n"
        self._file.write(text)

    def _do_alert(self, text, separator):
        text = f"{dt.now().strftime(self._dt_format)} - ALERT: {text}"
        if separator:
            text += f"\n{LOG_SEPARATOR}"
        text += f"\n"
        self._file.write(text)

    def _do_debug(self, text, separator):
        text = f"{dt.now().strftime(self._dt_format)} - DEBUG: {text}"
        if separator:
            text += f"\n{LOG_SEPARATOR}"
        text += f"\n"
        self._file.write(text)

