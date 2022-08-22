from db.run_sql import run_sql

from models.client_model import Client
from models.dog_model import Dog
from models.staff_model import Staff
import repositories.client_repo as client_repo


def select(id):
    client = None
    sql = "SELECT * from dogs WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        owner = client_repo.select(result['owner'])
        dog = Dog(result['name'], result['description'],
                  result['breed'], result['dob'], result['neutered'], result['vaccinations'],
                  result['checked_in'], result['staff'], result['image'], owner, result['id'])
        return dog


def select_all():
    dogs = []
    sql = "SELECT * from dogs"
    results = run_sql(sql)

    for row in results:
        owner = client_repo.select(row['owner'])
        dog = Dog(row['name'], row['description'],
                  row['breed'], row['dob'], row['neutered'], row['vaccinations'],
                  row['checked_in'], row['staff'], row['image'], owner, row['id'])
        dogs.append(dog)
    return dogs


def save(dog):
    sql = "INSERT INTO dogs(name, description, breed, dob, neutered, vaccinations, checked_in, staff, image, owner) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [dog.name, dog.description,
              dog.breed, dog.dob, dog.neutered, dog.vaccinations, dog.checked_in, dog.staff, dog.image, dog.owner]
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
              dog.breed, dog.dob, dog.neutered, dog.vaccinations, dog.checked_in, dog.staff, dog.image, dog.owner, dog.id]
    run_sql(sql, values)


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
