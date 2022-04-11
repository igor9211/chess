from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

import view


# creating the flask app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chess_sqlalchemy.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# creating an API object
api = Api(app)


api.add_resource(view.List, '/<figure>/<field>')
api.add_resource(view.Validate, '/<figure>/<field>/<dest_field>')

if __name__ == '__main__':
    app.run(debug=True)