
from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form= """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method = "POST">
        <label> Rotate by </label>
            <input type="text" name="rot" value="0"> 
        
            <textarea name="text">{0}</textarea>
            <input type="submit"/>


    </body>
</html>
"""
@app.route("/", methods=['POST'])
def encrypt():
    rotate = int(request.form['rot'])
    rotate_text = request.form['text']
    # use rotate_string function to rotate string
    rotated_string = rotate_string(rotate_text, rotate) 

    return '<h1>' + form.format(rotated_string) + '</h1>'

    # return rotated_string


@app.route("/")
def index():
    return form.format("")






app.run()


