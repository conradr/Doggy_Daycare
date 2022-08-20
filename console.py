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

#client_repo.save(client1)
# print(client_repo.select(3).__dict__)
#client_repo.delete(client1)
