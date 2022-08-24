from db.run_sql import run_sql

from models.client_model import Client
from models.dog_model import Dog
from models.staff_model import Staff
from models.report_model import Report
import repositories.client_repo as client_repo
import repositories.staff_repo as staff_repo
import repositories.dog_repo as dog_repo


def select(id):
    staff = None
    dog = None
    sql = "SELECT * from reports WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        staff = staff_repo.select(result['staff_id'])
        dog = dog_repo.select(result['dog_id'])
        report = Report(result['description'], dog, staff, result['id'])
        return report


def select_all():
    reports = []
    sql = "SELECT * from reports"
    results = run_sql(sql)

    for row in results:
        staff = staff_repo.select(row['staff_id'])
        dog = dog_repo.select(row['dog_id'])
        report = Report(row['description'], dog, staff, row['id'])
        reports.append(report)
    return reports


def save(report):
    sql = "INSERT INTO reports(dog_id, staff_id, description) VALUES (%s, %s, %s) RETURNING id"
    values = [report.dog.id, report.staff.id,
              report.description]
    result = run_sql(sql, values)
    report.id = result[0]['id']
    return report


def delete(report):
    sql = "DELETE FROM reports WHERE id = %s"
    values = [report.id]
    run_sql(sql, values)


def update(report):
    sql = "UPDATE reports SET (dog_id, staff_id, description) = (%s, %s, %s) WHERE id = %s"
    values = [report.dog.id, report.staff.id, report.description, report.id]
    result = run_sql(sql, values)
    return result


def get_comments_by_dog(dog):
    sql = "select dogs.id, comments.comment from comments join dogs ON dogs.id = comments.dog_id where comments.dog_id = %s"
    values = [dog.id]
    result = run_sql(sql, values)
    return result


def save_comment(comment):
    sql = "INSERT INTO comments(dog_id, staff_id, comment) VALUES (%s,%s,%s) returning id"
    values = [comment.dog.id, comment.staff.id, comment.comment]
    result = run_sql(sql, values)
    comment.id = result[0]['id']
    return comment


# def get_comments_by_do_id(id):
#     sql_comment_on_dog_by_id = "SELECT comment from comments WHERE dog_id = 1"
#     sql_comment_by_staff = "select staff.name, comments.comment from comments join staff on staff.id = comments.staff_id where staff.id = 1"


# def show_dogs_owner():
#     dogs_owner = []
#     sql = "SELECT clients.* FROM clients INNER JOIN dogs ON dogs.owner = clients.id WHERE dogs.id = %s"
#     values = [id]
#     result = run_sql(sql, values)
#     for row in result:
#         dog = Dog(row['name'], row['description'],
#                   row['breed'], row['dob'], row['neutered'], row['vaccinations'], row['checked_in'], 1, row['image'], 1, row['id'])
#         dogs_owner.append(dog)
#     return dogs_owner
