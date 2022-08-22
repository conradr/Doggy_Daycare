from db.run_sql import run_sql

from models.client_model import Client
from models.dog_model import Dog
from models.staff_model import Staff


def select(id):
    result = None
    sql = "SELECT * from staff WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        staff = Staff(result['name'], result['id'])
        return staff


def select_all():
    staff_members = []
    sql = "SELECT * from staff"
    results = run_sql(sql)

    for row in results:
        staff_person = Staff(row['name'], row['id'])
        staff_members.append(staff_person)
    return staff_members
