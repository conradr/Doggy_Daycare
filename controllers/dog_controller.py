from flask import Flask, render_template, request, redirect, flash
from flask import Blueprint
from models.client_model import Client
from models.dog_model import Dog
from models.staff_model import Staff
import repositories.dog_repo as dog_repo
import repositories.client_repo as client_repo
import repositories.staff_repo as staff_repo
from random import randint

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


@dog_blueprint.route('/dogs/<id>', methods=['POST'])
def save_update_dog(id):
    random_number = randint(0, 30)
    dog_image = f"https://placedog.net/110/200/?id={random_number}"
    dog_name = request.form['dog_name']
    dog_breed = request.form['dog_breed']
    dog_description = request.form['dog_description']
    dog_dob = request.form['dog_dob']
    dog_neutered = request.form['dog_neutered']
    dog_vaccinations = request.form['dog_vaccinations']
    dog_owner = client_repo.select(request.form['dog_owner'])
    dog_checked_in = request.form['dog_checked_in']
    staff_responsible = staff_repo.select(request.form['staff_responsible'])
    dog = Dog(dog_name, dog_description, dog_breed, dog_dob, dog_neutered,
              dog_vaccinations, dog_checked_in, staff_responsible, dog_image, dog_owner, id)
    print(dog.__dict__)
    dog_repo.update_dog(dog)
    flash(f" {dog.name} updated", "info")
    return redirect('/dogs')


@dog_blueprint.route('/dogs/<id>/checkin', methods=['POST'])
def check_dog_in_from_daycare(id):
    dog_object = dog_repo.check_dog_in_or_out(id)
    dog_repo.update_dog(dog_object)
    flash(f" {dog_object.name} checked in", "info")
    return redirect('/dogs')
    # redirect_url = f'/dogs/{id}'
    # return redirect(redirect_url)


@dog_blueprint.route('/dogs/<id>/checkout', methods=['POST'])
def check_dog_out_from_daycare(id):
    dog_object = dog_repo.check_dog_in_or_out(id)
    dog_repo.update_dog(dog_object)
    flash(f" {dog_object.name} checked out", "info")
    return redirect('/dogs')


@dog_blueprint.route('/dogs/new')
def new_dog_form():
    client_list = client_repo.select_all()
    staff_list = staff_repo.select_all()
    return render_template('dogs/dog_new.html', client_list=client_list, staff_list=staff_list)


@dog_blueprint.route('/dogs/new', methods=['POST'])
def save_dog():
    random_number = randint(0, 30)
    dog_image = f"https://placedog.net/110/200/?id={random_number}"
    dog_name = request.form['dog_name']
    dog_breed = request.form['dog_breed']
    dog_description = request.form['dog_description']
    dog_dob = request.form['dog_dob']
    dog_neutered = request.form['dog_neutered']
    dog_vaccinations = request.form['dog_vaccinations']
    dog_owner = client_repo.select(request.form['dog_owner'])
    dog_checked_in = request.form['dog_checked_in']
    staff_responsible = staff_repo.select(request.form['staff_responsible'])
    dog = Dog(dog_name, dog_description, dog_breed, dog_dob, dog_neutered,
              dog_vaccinations, dog_checked_in, staff_responsible, dog_image, dog_owner)
    print(dog.__dict__)
    dog_repo.save(dog)
    flash(f" {dog.name} saved!", "info")
    return redirect('/dogs')
