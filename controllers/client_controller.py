from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.client_model import Client
from models.dog_model import Dog
from models.staff_model import Staff
import repositories.client_repo as client_repo

client_blueprint = Blueprint("client", __name__)


@client_blueprint.route('/clients')
def all_clients():
    clients = client_repo.select_all()
    return render_template('clients/clients_index.html', clients=clients)


@client_blueprint.route('/clients/<id>/update', methods=['GET'])
def show_author_edit(id):
    client_object = client_repo.select(id)
    # ar.update_author_by_object(author_object)
    # authors = ar.show_all_authors()
    return render_template('clients/client_edit.html', client=client_object)


@client_blueprint.route('/clients/<id>', methods=['POST'])
def save_update_client(id):
    client_name = request.form['client_name']
    client_tel = request.form['client_tel']
    client_email = request.form['client_email']
    client_address = request.form['client_address']
    client_notes = request.form['client_notes']
    client = Client(client_name, client_tel, client_email,
                    client_address, client_notes, id)
    # author = ar.select_author_by_id(id)
    # author_object = Author[author_name, id]
    client_repo.update_client(client)
    return redirect('/clients')


@client_blueprint.route('/clients/<id>/delete', methods=['POST'])
def delete_client(id):
    client_object = client_repo.select(id)
    client_repo.delete(client_object)
    return redirect('/clients')
