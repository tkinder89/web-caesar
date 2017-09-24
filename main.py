from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form ="""
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
        <title>Web Caesar</title>
    </head>

    <body>
        <form method="post">
            Rotate by:
            <input type="text" name="rot" value="0">
            </br>
            <textarea name="text">
            </textarea>
            </br>
            <button type="submit">Submit Query</button>
        </form>
    </body>
</html>
"""

@app.route("/", methods=["POST"])
def encrypt():
    rotate_num = request.form['rot']
    rotate_num = int(rotate_num)

    rotate_text = request.form['text']

    result = rotate_string(rotate_text, rotate_num)

    return '<h1>' + result + '</h1>'
    


@app.route("/")
def index():
    return form

app.run()