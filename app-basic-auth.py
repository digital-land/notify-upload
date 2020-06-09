import os
from flask import Flask
from flask_basicauth import BasicAuth

import notify_upload


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

app.config["BASIC_AUTH_USERNAME"] = os.environ.get("BASIC_AUTH_USERNAME")
app.config["BASIC_AUTH_PASSWORD"] = os.environ.get("BASIC_AUTH_PASSWORD")

basic_auth = BasicAuth(app)


@app.route("/notify-upload", methods=["GET", "POST"])
@basic_auth.required
def notify_upload_file():
    return notify_upload.notify_upload()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
