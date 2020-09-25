import os

import flask

app = flask.Flask(__name__)

PORT = 80


@app.route("/", methods=["GET"])
def index():
    return (
        "<h1>Hello world!!! I have been deployed using docker and github actions</h1>"
    )


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT, debug=True)
