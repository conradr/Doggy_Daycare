from flask import Flask, render_template, request, redirect, flash
from flask import Blueprint
from models.client_model import Client
from models.dog_model import Dog
from models.staff_model import Staff
from models.report_model import Report
from models.comment_model import Comment

import repositories.report_repo as report_repo
import repositories.dog_repo as dog_repo
import repositories.staff_repo as staff_repo


report_blueprint = Blueprint("report", __name__)


@report_blueprint.route('/reports')
def all_reports():
    reports = report_repo.select_all()
    return render_template('reports/report_index.html', reports=reports)


@report_blueprint.route('/comment/<id>/add', methods=['POST'])
def save_update_comment(id):
    dog = dog_repo.select(request.form['dog_id'])
    staff = staff_repo.select(request.form['staff_id'])
    comment = request.form['comment']
    comment_object = Comment(staff, dog, comment)
    print(comment_object.__dict__)
    report_repo.save_comment(comment_object)
    #report_object = report_repo.select(id)
    #comments = report_repo.get_comments_by_dog(report_object.dog)
    flash(f"Comment added! ", "info")
    redirect_url = f'/reports/{id}'
    return redirect(redirect_url)

# @report_blueprint.route('/clients/<id>/update', methods=['GET'])
# def show_author_edit(id):
#     client_object = client_repo.select(id)
#     clients_dogs = client_repo.show_clients_dogs(id)
#     # ar.update_author_by_object(author_object)
#     # authors = ar.show_all_authors()
#     return render_template('clients/client_edit.html', client=client_object, clients_dogs=clients_dogs)


# @report_blueprint.route('/clients/<id>', methods=['POST'])
# def save_update_client(id):
#     client_name = request.form['client_name']
#     client_tel = request.form['client_tel']
#     client_email = request.form['client_email']
#     client_address = request.form['client_address']
#     client_notes = request.form['client_notes']
#     client = Client(client_name, client_tel, client_email,
#                     client_address, client_notes, id)
#     client_repo.update_client(client)
#     flash(f" {client.name} updated", "info")

#     return redirect('/clients')


@report_blueprint.route('/reports/<id>', methods=['GET'])
def show_report(id):
    report_object = report_repo.select(id)
    comments = report_repo.get_comments_by_dog(report_object.dog)
    return render_template('reports/report_show.html', report=report_object, comments=comments)


# @report_blueprint.route('/clients/<id>/delete', methods=['POST'])
# def delete_client(id):
#     client_object = client_repo.select(id)
#     client_repo.delete(client_object)
#     return redirect('/clients')


# @report_blueprint.route('/clients/new')
# def new_client_form():
#     clients = client_repo.select_all()
#     return render_template('clients/client_new.html', clients=clients)


# @client_blueprint.route('/clients/new', methods=['POST'])
# def save_new_client():
#     client_name = request.form['client_name']
#     client_tel = request.form['client_tel']
#     client_email = request.form['client_email']
#     client_address = request.form['client_address']
#     client_notes = request.form['client_notes']
#     client = Client(client_name, client_tel, client_email,
#                     client_address, client_notes)
#     # author = ar.select_author_by_id(id)
#     # author_object = Author[author_name, id]
#     client_repo.save(client)
#     return redirect('/clients')
