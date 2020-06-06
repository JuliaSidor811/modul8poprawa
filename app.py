from flask import Flask, request, render_template
from datetime import time

app = Flask(__name__)


def my_render_template(html_page_path, **kwargs):
    kwargs['timestamp'] = time()
    return render_template(html_page_path, **kwargs)


@app.route('/')
def main_page():
    return my_render_template("main_page.html")


@app.route('/me')
def about_me():
    return my_render_template("about_me.html")


@app.route('/contact', methods=['GET'])
def contact():
    return my_render_template("contact.html")


@app.route('/contactme', methods=['GET', 'POST'])
def contact_sheet():
    if request.method == 'POST':
        data = request.form
        username = str(data.get("firstname"))
        if len(username) > 0:
            return f"Dziękujemy {username}"
        else:
            return f"Nie podano imienia"

    return my_render_template("contact_me.html")


if __name__ == '__main__':
    app.run()
