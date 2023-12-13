"""Seed file to make sample data for users db."""

from models import Department, Employee, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Add users
d1 = Department(dept_code="mktg", dept_name="Marketing", phone="897-9999")
d2 = Department(dept_code="acct", dept_name="Accounting", phone="111-5429")
d3 = Department(dept_code="r&d", dept_name="Research and Devlopment", phone="908-7878")
d4 = Department(dept_code="sales", dept_name="Sales", phone="225-6912")
d5 = Department(dept_code="it", dept_name="Information Technology", phone="888-4562")

river = Employee(name="River Bottom", state="NY", dept_code="mktg")
summer = Employee(name="Summer Winter", state="OR", dept_code="mktg")
jaoquin = Employee(name="Jaoquin Phoenix", dept_code="acct")
octavia = Employee(name="Octavia Spencer", dept_code="r&d")
larry = Employee(name="Larry David", dept_code="r&d", state="NY")
kurt = Employee(name="Kurt Cobain", dept_code="it", state="WA")
rain = Employee(name="River Phoenix", dept_code="it")

# If table isn't empty, empty it
# User.query.delete()


# Add new objects to session, so they'll persist
# db.session.add (d1)
# db.session.add (d2)
# db.session.add (d3)
# db.session.add (d4)
db.session.add_all([d1,d2,d3,d4,d5])

# db.session.commit()


# db.session.add (river)
# db.session.add (summer)
# db.session.add (jaoquin)
# db.session.add (octavia)
# db.session.add (larry)
# db.session.add (kurt)
# db.session.add (rain)
db.session.add_all([river, summer, jaoquin, octavia, larry, kurt, rain])

# Commit--otherwise, this never gets saved!
db.session.commit()