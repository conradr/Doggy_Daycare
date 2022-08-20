from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.client_model import Client
from models.dog_model import Dog
from models.staff_model import Staff
import repositories.staff_repo as staff_repo

staff_blueprint = Blueprint("staff", __name__)
