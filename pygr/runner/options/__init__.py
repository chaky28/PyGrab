from selenium.webdriver import ChromeOptions
from pygr.definition import Definition


def get_default_options():
    driver_option = ChromeOptions()
    driver_option.add_argument("--disable-dev-shm-usage")
    driver_option.add_argument('--ignore-ssl-errors=yes')
    driver_option.add_argument('--ignore-certificate-errors')
    # driver_option.add_argument('--headless')
    driver_option.add_argument("--window-size=1600,1600")
    driver_option.add_argument("--disable-application-cache")
    driver_option.add_argument("--no-sandbox")
    driver_option.add_argument("--lang=en")
    return driver_option


class Options:
    def __init__(self):
        self._driver_options = get_default_options()

    def get(self, definition: Definition):
        options = definition.get("general.browser")
        if not options:
            return self._driver_options

        for k, v in options.items():
            if k == "window_size":
                self._driver_options.add_argument(f"--window-size={v}")
            if k == "headless" and v:
                self._driver_options.add_argument(f"--headless")
            if k == "language":
                self._driver_options.add_argument(f"--lang={v}")
            if k == "ignore-ssl" and not v:
                self._driver_options.add_argument(f"--ignore-ssl-errors=no")

        return self._driver_options
