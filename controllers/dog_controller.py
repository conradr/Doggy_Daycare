from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.client_model import Client
from models.dog_model import Dog
from models.staff_model import Staff
import repositories.dog_repo as dog_repo
import repositories.client_repo as client_repo
import repositories.staff_repo as staff_repo

dog_blueprint = Blueprint("dog", __name__)


@dog_blueprint.route('/dogs')
def all_dogs():
    dogs = dog_repo.select_all()
    return render_template('dogs/dog_index.html', dogs=dogs)


@dog_blueprint.route('/dogs/<id>', methods=['GET'])
def show_dog(id):
    dog_object = dog_repo.select(id)
    return render_template('dogs/dog_show.html', dog=dog_object)


@dog_blueprint.route('/dogs/<id>/update', methods=['GET'])
def show_dog_edit(id):
    dog_object = dog_repo.select(id)
    all_clients = client_repo.select_all()
    all_staff = staff_repo.select_all()
    return render_template('dogs/dog_edit.html', dog=dog_object, all_clients=all_clients, all_staff=all_staff)


@dog_blueprint.route('/dogs/<id>/checkin_out', methods=['POST'])
def check_dog_in_or_out_from_daycare(id):
    dog_object = dog_repo.check_dog_in_or_out(id)
    dog_repo.update_dog(dog_object)
    return render_template('dogs/dog_edit.html', dog=dog_object)
