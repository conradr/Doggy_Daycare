from models.client_model import Client
from models.dog_model import Dog
from models.staff_model import Staff
import repositories.client_repo as client_repo
import repositories.dog_repo as dog_repo
import repositories.staff_repo as staff_repo


# print(client_repo.select(1).__dict__)

# client_list = client_repo.select_all()
# for client in client_list:
#    print(client.__dict__)

client1 = Client('Fran FurFur', '07884969585', 'fran@furfur.com',
                 '33b Bow Wow Place, Edinburgh', 'Slightly neurotic with a unique laugh')

dog1 = Dog('Salty', 'Cute little scruffy thing', 'Spaniel', '2011-10-25',
           True, 'Puppy, Kennel Cough', False, 1, 'https://placedog.net/15/200', 2)

# client_repo.save(client1)
# print(client_repo.select(3).__dict__)
# client_repo.delete(client1)
#client_list = client_repo.show_clients_dogs(2)
# for client in client_list:
#    print(client.__dict__)

# print(dog_repo.select(2).__dict__)

#dog_list = dog_repo.select_all()
# for dog in dog_list:
#    print(dog.__dict__)

dog_repo.save(dog1)
