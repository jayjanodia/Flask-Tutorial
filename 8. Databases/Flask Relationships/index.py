# CREATE ENTRIES INTO TABLES

from models import Owner, Puppy, Toy, db

# CREATING 2 PUPPIES

rufus = Puppy("Rufus")
fido = Puppy("Fido")

# ADD PUPPIES TO DB
db.session.add_all([rufus, fido])
db.session.commit()

# CHECK
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name="Rufus").first()
print(rufus)

# CREATE OWNER

jose = Owner("Jose", rufus.id)

# GIVE RUFUS TOYS
toy1 = Toy("Chew Toy", rufus.id)
toy2 = Toy("Ball", rufus.id)

# ADD ITEMS TO MULTIPLE TABLES USING ADD_ALL
db.session.add_all([jose, toy1, toy2])
db.session.commit()

# GRAB RUFUS AFTER ADDITIONS
rufus = Puppy.query.filter_by(name="Rufus").first()
print(rufus)

rufus.report_toys()
