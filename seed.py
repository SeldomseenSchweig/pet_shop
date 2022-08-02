from models import Pet, db, connect_db 
from app import app

db.drop_all()
db.create_all()

dog = Pet(name='sparky',species='dog', age=3)
cat =  Pet(name='tab',species='cat', age=4)
cat2 =  Pet(name='mot',species='cat', age=1)
dog2 =  Pet(name='chop',species='dog', age=2)
db.session.add(dog)
db.session.add(cat)
db.session.add(dog2)
db.session.add(cat2)
db.session.commit()