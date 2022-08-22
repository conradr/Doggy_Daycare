from db.run_sql import run_sql

from models.client_model import Client
from models.dog_model import Dog
from models.staff_model import Staff


def select(id):
    result = None
    sql = "SELECT * from clients WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        client = Client(result['name'], result['tel'],
                        result['email'], result['address'], result['notes'], result['id'])
        return client


def select_all():
    clients = []
    sql = "SELECT * from clients"
    results = run_sql(sql)

    for row in results:
        client = Client(row['name'], row['tel'],
                        row['email'], row['address'], row['notes'], row['id'])
        clients.append(client)
    return clients


def save(client):
    sql = "INSERT INTO clients(name, tel,  email, address, notes) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [client.name, client.tel,
              client.email, client.address, client.notes]
    result = run_sql(sql, values)
    client.id = result[0]['id']
    return client


def delete(client):
    sql = "DELETE FROM clients WHERE id = %s"
    values = [client.id]
    run_sql(sql, values)


def update_client(client):
    sql = "UPDATE clients SET (name, tel,  email, address, notes) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [client.name, client.tel,
              client.email, client.address, client.notes, client.id]
    run_sql(sql, values)


def show_clients_dogs(id):
    clients_dogs = []
    sql = "SELECT dogs.* FROM dogs INNER JOIN clients ON clients.id = dogs.owner WHERE clients.id = %s"
    values = [id]
    result = run_sql(sql, values)
    for row in result:
        dog = Dog(row['name'], row['description'],
                  row['breed'], row['dob'], row['neutered'], row['vaccinations'], row['checked_in'], 1, row['image'], 1, row['id'])
        clients_dogs.append(dog)
    return clients_dogs
