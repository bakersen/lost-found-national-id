from distutils.log import debug
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLAlchemy_DATABASE_URI'] = 'mysql://root:''@localhost/national_id'

db = SQLAlchemy(app)

@app.route('/')
def hello():
    return "Hello World"



if __name__ == "__main__":
    app.run(debug=True)