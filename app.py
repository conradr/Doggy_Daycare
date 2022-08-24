from flask import Flask, render_template

from controllers.client_controller import client_blueprint
from controllers.dog_controller import dog_blueprint
from controllers.staff_controller import staff_blueprint
from controllers.report_controller import report_blueprint
import repositories.dog_repo as dog_repo
import repositories.client_repo as client_repo
import repositories.staff_repo as staff_repo
import repositories.report_repo as report_repo

app = Flask(__name__)
app.secret_key = "hello"

app.register_blueprint(client_blueprint)
app.register_blueprint(staff_blueprint)
app.register_blueprint(dog_blueprint)
app.register_blueprint(report_blueprint)


@app.route('/')
def home():
    dogs = dog_repo.select_all()
    staff = staff_repo.select_all()
    clients = client_repo.select_all()
    return render_template('index.html', dogs=dogs, staff=staff, clients=clients)


if __name__ == '__main__':
    app.run(debug=True)
