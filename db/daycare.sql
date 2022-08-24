DROP TABLE comments CASCADE;
DROP TABLE daycare CASCADE;
DROP TABLE staff CASCADE;
DROP TABLE clients CASCADE;
DROP TABLE reports CASCADE;
DROP TABLE dogs CASCADE;


CREATE TABLE daycare (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

INSERT INTO daycare (name) VALUES ('Scratchies');

CREATE TABLE staff (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

INSERT INTO staff (name) VALUES ('Sammy Scratchworth');
INSERT INTO staff (name) VALUES ('Felicia Fleabody');

CREATE TABLE clients (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255), 
  tel TEXT,
  email VARCHAR(255),
  address TEXT,
  notes TEXT
);

INSERT INTO clients (name, tel, email, address, notes) VALUES ('Mary Brooks', '07447125447', 'mary@brooks.com', '48 Brenda Heights, Edinburgh','Loves her dog Flora' );
INSERT INTO clients (name, tel, email, address, notes) VALUES ('Farook Border', '07447125232', 'farook@border.com', '35 Furry Paws Lane, Glasgow','Looks a bit like his dog' );


CREATE TABLE dogs (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description TEXT,
  breed VARCHAR(255),
  dob VARCHAR(255),
  neutered BOOLEAN,
  vaccinations TEXT,
  checked_in BOOLEAN,
  staff INT REFERENCES staff(id),
  image VARCHAR(255),
  owner INT REFERENCES clients(id) ON DELETE CASCADE
);


INSERT INTO dogs (name, description, breed, dob, neutered, vaccinations, checked_in, staff, image, owner) VALUES ('Flora', 'brown with a cute button nose, can be a little nervous','Cavapoo', '2019-05-25', TRUE,'Puppy, Leprospirosis, Kennel Cough', FALSE, 1 , 'https://placedog.net/125/200', 1);

INSERT INTO dogs (name, description, breed, dob, neutered, vaccinations, checked_in, staff, image, owner) VALUES ('Sammy', 'Terrier with an attitude. Loves belly rubs.','Border Terrier', '2016-03-14', TRUE, 'Puppy, Leprospirosis, Distemper', FALSE, 2 , 'https://placedog.net/109/200', 2);

INSERT INTO dogs (name, description, breed, dob, neutered, vaccinations, checked_in, staff, image, owner) VALUES ('Fifi', 'Fox Red with a white spot on her tail. Attitude of a great dane','Bichon Frise', '2013-02-16', TRUE,'Puppy, Leprospirosis, Kennel Cough', FALSE, 1 , 'https://placedog.net/110/200', 1);

CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  dog_id INT REFERENCES dogs(id),
  staff_id INT REFERENCES staff(id),
  comment TEXT
);

INSERT INTO comments(dog_id, staff_id, comment) VALUES (1,1,'Flora is such a wee sweetie. She had a lovely day today');
INSERT INTO comments(dog_id, staff_id, comment)VALUES (2,1,'Sammy played with Flora today, he had such a fun time coming out of his shell');
INSERT INTO comments(dog_id, staff_id, comment)VALUES (1,2,'Flora loved her play time with Sammy, she really helped Sammy come out of his shell');

CREATE TABLE reports (
  id SERIAL PRIMARY KEY,
  dog_id INT REFERENCES dogs(id),
  staff_id INT REFERENCES staff(id),
  description TEXT
);

INSERT INTO reports(dog_id, staff_id, description) VALUES (1,1,'Amazing day at the madhouse today. She really came out of her shell!');
INSERT INTO reports(dog_id, staff_id, description) VALUES (2,1,'Couldnt fault fluffy today. She was a superstar');