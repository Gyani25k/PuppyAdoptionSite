from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

x="Gyani@123"

hashed_password = bcrypt.generate_password_hash(x)

# print(hashed_password)

check = bcrypt.check_password_hash(hashed_password,"Gyani@123")

print(check)

