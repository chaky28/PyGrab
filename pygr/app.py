import time
import requests
from flask import Flask, render_template
from pygr.browser import Browser
from pygr.definition import Definition
from pygr.runner import Options
from pygr.common import set_browser_ui, set_log_filepath, MAX_RETRIES
from pygr.common.logger import Logger
import threading


def create_app():
    flask_app = Flask(__name__)

    # --------------------------------------------------------------------------- #
    # Register Blueprints

    from app_ui import bp as ui_bp
    flask_app.register_blueprint(ui_bp)

    # --------------------------------------------------------------------------- #

    @flask_app.route("/")
    def home():
        return render_template("home.html")

    return flask_app


# --------------------------------------------------------------------------- #


def initialize_ui():
    localhost = "http://localhost:5000"
    request = requests.get(localhost)
    retries = 0
    while not request.ok and retries <= MAX_RETRIES:
        retries += 1
        time.sleep(0.5)
        request = requests.get(localhost)

    if not request.ok:
        raise Exception("Max retires waiting for local server to be online.")

    options = Options(is_headless=False).get(Definition({}))
    options.add_argument(f"--app={localhost}")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    browser = Browser(options)
    browser.browser.maximize_window()
    set_browser_ui(browser)

    with Logger("UI") as logger:
        set_log_filepath(logger.get_filepath())


if __name__ == "__main__":
    thread = threading.Thread(target=initialize_ui)
    thread.start()

    app = create_app()
    app.run()

