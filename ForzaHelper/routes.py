from flask import render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from ForzaHelper import app, db
from ForzaHelper.models import User, login_manager, CarSettingsCard
from json_opener import JsonFiles


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/profile')
@login_required
def profile():
    user_id = current_user.get_id()
    user = User.query.filter_by(id=user_id).first()
    return render_template('profile.html', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
        user = User.query.filter_by(login=login).first()

        if user and check_password_hash(user.password, password):
            login_user(user)

            return redirect(url_for('index'))
        else:
            flash('Login or password is not correct')
    else:
        flash('Please fill login and password fields')

    return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':
        if not (login or password or password2):
            flash('Please fill all fields')
        elif password != password2:
            flash('Passwords are not equal')
        elif User.query.filter_by(login=login).first():
            flash('This login is already using')
        else:
            hash_password = generate_password_hash(password)
            new_user = User(login=login, password=hash_password)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('login_page'))

    return render_template('register.html')


@app.route('/settings')
def car_settings():
    brand_values = JsonFiles.brand_list
    model_values = JsonFiles.model_list
    car_settings_cards = CarSettingsCard.query.order_by(CarSettingsCard.id).all()

    return render_template('settings.html', brand_values=brand_values, model_values=model_values, car_settings_cards=car_settings_cards)


@app.route('/add-car-setting', methods=['GET', 'POST'])
@login_required
def add_car_setting():

    brand_values = JsonFiles.brand_list
    model_values = JsonFiles.model_list

    if request.method == "POST":
        setting_name = request.form.get('setting-name')
        car_class = request.form.get('car-class')
        brand = request.form.get('car-brand')
        model = request.form.get('car-model')
        setting_id = request.form.get('setting-id')
        setting_description = request.form.get('setting-description')
        user_id = current_user.id

        car_name = JsonFiles.get_name_by_model(model)

        if request.method == 'POST':
            if not (setting_name and car_class and brand and model and setting_id):
                flash('Please fill all fields')
            elif brand not in brand_values:
                flash('You wrongly typed the brand of the car\nPlease retype it again')
            elif model not in model_values:
                flash('You wrongly typed the model of the car\nPlease retype it again')
            elif car_class == 'Class':
                flash('You didn\'t choose the class of the car')
            else:
                car_setting = CarSettingsCard(brand=brand, model=model, car_class=car_class, setting_id=setting_id, setting_name=setting_name, setting_description=setting_description, added_by=user_id, car_name=car_name)
                db.session.add(car_setting)
                db.session.commit()

    return render_template('add_car_setting.html', brand_values=brand_values, model_values=model_values)


@app.route('/designs')
def car_designs():
    return render_template('designs.html')


@app.route('/car-park')
@login_required
def car_park():
    return render_template('car-park.html')


@app.route('/print-users')
def print_users():
    users = User.query.order_by(User.id).all()
    return render_template('print_users.html', users=users)


@app.route('/print-settings')
def print_settings():
    settings = CarSettingsCard.query.order_by(CarSettingsCard.id).all()
    return render_template('print_settings.html', settings=settings)


@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login_page'))
    return response


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html'), 404
