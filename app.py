from crypt import methods
from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, Pet
from forms import PetForm, EditPetForm



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route('/')
def list_pets():
    """Lists pets"""
    pets = Pet.query.all()
    return render_template("list_of_pets.html", pets=pets)


@app.route('/add', methods=["POST", "GET"])
def add_pet_form():
    """shows and handles form to add pet"""
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name = name, species=species, photo_url=photo_url, age=age,notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)



@app.route('/<int:id>', methods=["GET", "POST"])
def edit_form(id):
    """show and handles form to edit petEdits pet"""
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.is_available = form.is_available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit_pet_form.html', form=form, id=id)


    
    

