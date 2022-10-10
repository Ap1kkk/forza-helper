from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from waitress import serve

app = Flask(__name__)
app.secret_key = 'some secret salt'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fhelper.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)

from ForzaHelper import models, routes

db.create_all()
app.run(debug=True)
# app.run(debug=False, host='0.0.0.0', port=80)
# serve(app, port=8080)