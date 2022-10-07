from flask_login import UserMixin

from ForzaHelper import db, login_manager


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)


class CarSettingsCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(68), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    car_class = db.Column(db.String(4), nullable=False)
    setting_id = db.Column(db.String(30), nullable=False)
    setting_name = db.Column(db.String(100), nullable=False)
    setting_description = db.Column(db.String(300))
    added_by = db.Column(db.Integer, nullable=False)
    car_name = db.Column(db.String(30), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


