from index import db, Puppy

# CREATE
if len(Puppy.query.filter_by(name='Rufus').all()) == 0:
    my_puppy = Puppy('Rufus', 5)
    db.session.add(my_puppy)
    db.session.commit()

# READ
all_puppies = Puppy.query.all() # List of all puppy objects in the table
print(all_puppies)
print(db.session.get(Puppy, 1)) # Find by ID

# FILTER
puppy_franky = Puppy.query.filter_by(name="Franky").all()
print(puppy_franky)