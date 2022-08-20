from flask import Flask, render_template

from controllers.client_controller import client_blueprint
from controllers.dog_controller import dog_blueprint
from controllers.staff_controller import staff_blueprint

app = Flask(__name__)

app.register_blueprint(client_blueprint)
app.register_blueprint(staff_blueprint)
app.register_blueprint(dog_blueprint)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
