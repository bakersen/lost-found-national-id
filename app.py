from flask import Flask, jsonify, request
from distutils.log import debug
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/national_id'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Nationalid(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nin = db.Column(db.String(14), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    given_name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return self.id

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class NationalidSchema(Schema):
    id = fields.Integer()
    nin = fields.String()
    surname = fields.String()
    given_name = fields.String()



@app.route('/')
def hello():
    return "Hello World"

@app.route('/nationalid', methods=['GET'])

def get_all_nationalids():
    nin = Nationalid.get_all()
    serializer = NationalidSchema(many=True)
    data = serializer.dump(nin)

    return jsonify(
        data
    )

@app.route('/nationalid', methods=['POST'])

def register_nationalid():
    data = request.get_json()
    new_nationalid = Nationalid ( 
        nin=data.get('nin'),
        surname=data.get('surname'),
        given_name=data.get('given_name')
    )

    new_nationalid.save()

    serializer = NationalidSchema()

    data = serializer.dump(new_nationalid)

    return jsonify(
        data
    ), 201


@app.route('/nationalid/<int:id>', methods=['GET'])
def get_nationalid(id):
    pass


@app.route('/nationalid/<int:id>', methods=['PUT'])
def update_nationalid(id):
    pass


@app.route('/nationalid/<int:id>', methods=['DELETE'])
def delete_nationalid(id):
    pass



if __name__ == "__main__":
    app.run(debug=True)