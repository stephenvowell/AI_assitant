from flask import Flask, session, redirect, url_for, request
from models import db, User, Device  # Import your models and database setup
from config import DevelopmentConfig  # Import your configuration

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)  # Use the development configuration
db.init_app(app)

@app.route('/register_device', methods=['GET', 'POST'])
def register_device():
    if 'username' not in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        device_id = request.form['device_id']
        username = session['username']

        user = User.query.filter_by(username=username).first()
        if user is None:
            return redirect(url_for('home'))

        new_device = Device(device_id=device_id, user_id=user.id)
        db.session.add(new_device)
        db.session.commit()

        return redirect(url_for('dashboard'))

if __name__ == "__main__":
    app.run(debug=True)