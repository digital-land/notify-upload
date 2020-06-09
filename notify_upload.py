from flask import render_template, request

import notify

ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif", "csv"}


def notify_upload():
    if request.method == "POST":
        # check if the post request has the recipient email
        if "email" not in request.form:
            flash("No recipient email")
            return redirect(request.url)
        email = request.form.get("email")

        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            notify.send(file.stream, email)
            return """
            <!doctype html>
            <title>Uploaded File</title>
            <h1>Uploaded File</h1>
            URL has been sent via email
        """
    return input_form()


def input_form():
    return render_template("main.html")


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
