from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.client_model import Client
from models.dog_model import Dog
from models.staff_model import Staff
import repositories.dog_repo as dog_repo

dog_blueprint = Blueprint("dog", __name__)


@dog_blueprint.route('/dogs')
def all_dogs():
    dogs = dog_repo.select_all()
    return render_template('dogs/dog_index.html', dogs=dogs)
