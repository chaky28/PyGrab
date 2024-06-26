
DB_NAME = "pygr"
DB_HOST_DEV = "localhost"
DB_PORT_DEV = "5433"
DB_USER_DEV = "postgres"
DB_PASSWORD_DEV = "25898"

INTERNAL_LOADED_URL_LOCATOR_TYPE = "loaded_url"
INTERNAL_STARTING_URL_LOCATOR_TYPE = "starting_url"
INTERNAL_DATETIME_URL_LOCATOR_TYPE = "datetime"
XPATH_LOCATOR_TYPE = "XPATH"
CSS_LOCATOR_TYPE = "CSS"

BROWSER_MODE = "BROWSER"
CRAWLER_MODE = "CRAWLER"

URL_LIST_TYPE = "list"

EXCEL_EXPORT_FORMAT = "EXCEL"
CSV_EXPORT_FORMAT = "CSV"
EXPORT_FORMATS = ["CSV", "EXCEL"]

GRABBER_TYPE = "grabber"
GRABBER_LIST_TYPE = "grabber_list"
GRABBER_INTERNAL_TYPE = "grabber_internal"
PAGINATION_TYPE = "pagination"
NAVIGATION_TYPE = "navigation"

ITEMS_THAT_EXPORT = [GRABBER_TYPE, GRABBER_INTERNAL_TYPE]

CLICK_ACTION = "click"
LOAD_URL_ACTION = "load_url"

DEFAULT_EXPORT_ENCODING = "utf8"
DEFAULT_DATETIME_FORMAT = "%m/%d/%Y %H:%M:%S:%f"
DEFAULT_ITEM_NAME = "NO_NAME_SUPPLIED"

REGEX_TR_TYPE = "regex"

LOGS_FILE_PATH = "logs"
LOG_SEPARATOR = "--------------------------------------------------------------------------------------------------"

POSTGRES_CONN_TYPE = "postgres"

MAX_RETRIES = 20

# -------------------------- Browser and Log variables for UI --------------------------

browser_ui = None
log_filepath = ""


def set_browser_ui(browser):
    global browser_ui
    browser_ui = browser


def get_browser_ui():
    global browser_ui
    return browser_ui


def set_log_filepath(filepath):
    global log_filepath
    log_filepath = filepath


def get_log_filepath():
    global log_filepath
    return log_filepath
