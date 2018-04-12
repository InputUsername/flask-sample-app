import os
import flask_monitoringdashboard as dashboard

from flask import Flask, render_template, request, redirect, url_for
from db import add_user, get_all_users

app = Flask(__name__)
dashboard.config.outlier_detection_constant = 0.1
dashboard.config.database_name = os.environ.get('DASHBOARD_DATABASE_URL', 'sqlite:///flask_monitoringdashboard.db')
dashboard.bind(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', users=get_all_users())


@app.route('/user', methods=['POST'])
def user():
    add_user(request.form['name'], request.form['email'])
    return redirect(url_for('index'))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
