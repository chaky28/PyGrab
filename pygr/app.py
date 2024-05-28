from flask import Flask, render_template


def create_app():
    flask_app = Flask(__name__)

    # --------------------------------------------------------------------------- #
    # Register Blueprints

    # --------------------------------------------------------------------------- #

    @flask_app.route("/")
    def home():
        return render_template("home.html")

    return flask_app


# --------------------------------------------------------------------------- #

if __name__ == "__main__":
    app = create_app()
    app.run()
