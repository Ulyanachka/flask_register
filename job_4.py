from flask import Flask, render_template, flash, redirect
from form import RegistrationForm
from models import db, User
from flask_wtf.csrf import CSRFProtect

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///basejob4.db'
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app

app = create_app()
app.secret_key = b'a18995304586e38b23a71914e2046a3f5f5dc1fe9096e53623610fd9bcb7d9fe'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hello'


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect('/')
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)