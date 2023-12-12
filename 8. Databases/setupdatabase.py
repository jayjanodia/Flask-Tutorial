from index import db, Puppy, app

# Set up our database. Transforms the model class into the database table
db.create_all()

sam = Puppy('Sammy', 4)
frank = Puppy('Franky', 5)

# Should print None since you've not added the data to the table yet
print(sam.id, frank.id, sep='\n')

db.session.add_all([sam, frank])

# db.session.add(sam)
# db.session.add(frank)

db.session.commit()

print(sam.id, frank.id, sep='\n')