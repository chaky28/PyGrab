from flask import blueprints, request
from pygr.browser import Browser
from pygr.common.logger import Logger
from pygr.locator import Locator
from pygr.runner.options import get_default_options
from pygr.common import get_log_filepath
from pygr.transformer import Transformer

bp = blueprints.Blueprint("ui", __name__, url_prefix="/ui")
browser = Browser(get_default_options(is_headless=False))


@bp.route("/load-url", methods=["POST"])
def load_url():
    try:
        url = request.json.get("url")
        if not url:
            raise Exception("No url supplied.", 400)

        global browser
        with Logger("UI", full_filepath=get_log_filepath()) as logger:
            # Load URL
            browser.load_url(url, logger)

            # Add style tag to specify highlighting styles for pygr-selected attribute inside the header
            browser.browser.execute_script("document.head.insertAdjacentHTML('beforeend', '<style>[pygr-selected]{"
                                           "background-color: rgb(145 177 179) !important;"
                                           "color: black !important;border: 2px solid rgb(43 144 151) !important;"
                                           "border-radius: 5px !important;"
                                           "}</style>')")

        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "error": str(e)}, 500 if len(e.args) == 0 else e.args[1]


@bp.route("/highlight-and-grab", methods=["POST"])
def highlight_selection():
    try:
        body = request.json
        selectors = body.get("selectors")
        if not selectors or len(selectors) == 0:
            raise Exception("No selectors supplied.", 400)

        global browser
        s_browser = browser.browser

        # Remove previously selected elements
        s_browser.execute_script(
            "document.querySelectorAll('[pygr-selected]')?.forEach(e => e.removeAttribute('pygr-selected'))")

        with Logger("UI", full_filepath=get_log_filepath()) as logger:

            # Get all elements using selectors provided
            selections = [s_browser]
            for selector in selectors:
                partial_selections = []
                for selection in selections:
                    partial_selections += Locator(selector).process(selection, logger, find_all=True)
                selections = partial_selections

            data = []
            attribute = body.get("attribute", "textContent")
            if len(selections) > 0:
                # Scroll into view to the first selected element
                s_browser.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'})",
                                         selections[0])

                for selection in selections:
                    # Set attribute to highlight element
                    s_browser.execute_script(f"arguments[0].setAttribute('pygr-selected', '')", selection)

                    # Get data from selected elements
                    attr_value = selection.get_attribute(attribute)
                    data.append("" if not attr_value else attr_value.strip())

        return {"status": "ok", "data": data}
    except Exception as e:
        return {"status": "error", "error": str(e)}, 500 if len(e.args) == 0 else e.args[1]


@bp.route("/transform", methods=["POST"])
def transform():
    try:
        body = request.json
        transformation = body.get("transformation")
        if not transformation:
            raise Exception("No transformation supplied.", 400)

        data_to_transform = body.get("data")
        if not data_to_transform:
            raise Exception("No data to transform supplied.")

        with open(get_log_filepath()) as logger:
            return Transformer(transformation, data_to_transform).do(logger, only_get_first=False)

    except Exception as e:
        return {"status": "error", "error": str(e)}, 500 if len(e.args) == 0 else e.args[1]
