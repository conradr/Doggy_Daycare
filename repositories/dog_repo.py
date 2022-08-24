from db.run_sql import run_sql

from models.client_model import Client
from models.dog_model import Dog
from models.staff_model import Staff
import repositories.client_repo as client_repo
import repositories.staff_repo as staff_repo


def select(id):
    client = None
    staff_member = None
    sql = "SELECT * from dogs WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        client = client_repo.select(result['owner'])
        staff_member = staff_repo.select(result['staff'])
        dog = Dog(result['name'], result['description'],
                  result['breed'], result['dob'], result['neutered'], result['vaccinations'],
                  result['checked_in'], staff_member, result['image'], client, result['id'])
        return dog


def select_all():
    dogs = []
    sql = "SELECT * from dogs"
    results = run_sql(sql)

    for row in results:
        owner = client_repo.select(row['owner'])
        dog = Dog(row['name'], row['description'], row['breed'], row['dob'], row['neutered'],
                  row['vaccinations'], row['checked_in'], row['staff'], row['image'], owner, row['id'])
        dogs.append(dog)
    return dogs


def save(dog):
    sql = "INSERT INTO dogs(name, description, breed, dob, neutered, vaccinations, checked_in, staff, image, owner) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [dog.name, dog.description,
              dog.breed, dog.dob, dog.neutered, dog.vaccinations, dog.checked_in, dog.staff.id, dog.image, dog.owner.id]
    result = run_sql(sql, values)
    dog.id = result[0]['id']
    return dog


def delete(dog):
    sql = "DELETE FROM dogs WHERE id = %s"
    values = [dog.id]
    run_sql(sql, values)


def update_dog(dog):
    sql = "UPDATE dogs SET (name, description, breed, dob, neutered, vaccinations, checked_in, staff, image, owner) = (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [dog.name, dog.description,
              dog.breed, dog.dob, dog.neutered, dog.vaccinations, dog.checked_in, dog.staff.id, dog.image, dog.owner.id, dog.id]
    result = run_sql(sql, values)
    return result


def check_dog_in_or_out(id):
    dog_to_check_in = select(id)
    if dog_to_check_in.checked_in == False:
        dog_to_check_in.checked_in = True
    else:
        dog_to_check_in.checked_in = False
    return dog_to_check_in


def get_comments_by_do_id(id):
    sql_comment_on_dog_by_id = "SELECT comment from comments WHERE dog_id = 1"
    sql_comment_by_staff = "select staff.name, comments.comment from comments join staff on staff.id = comments.staff_id where staff.id = 1"


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
