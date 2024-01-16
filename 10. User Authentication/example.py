from flask_bcrypt import Bcrypt
from werkzeug.security import check_password_hash, generate_password_hash

# Creating hashing object
bcrypt = Bcrypt()
password = "supersecretpassword"
hashed_password = bcrypt.generate_password_hash(password=password)
check_true = bcrypt.check_password_hash(hashed_password, "supersecretpassword")
check_false = bcrypt.check_password_hash(hashed_password, "wrongpassword")
print(check_true)  # should be true
print(check_false)  # Should be false
print(hashed_password)


werkzeug_password = generate_password_hash("mypassword")
print(werkzeug_password)
check_true = check_password_hash(werkzeug_password, "mypassword")
check_false = check_password_hash(werkzeug_password, "wrongpassword")
print(check_false)
print(check_true)
