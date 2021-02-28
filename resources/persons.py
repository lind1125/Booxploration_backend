import models 

from flask import Blueprint, jsonify, request, session, make_response
from playhouse.shortcuts import model_to_dict
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required


persons = Blueprint('persons', 'persons')

@persons.route('/profile', methods=['GET'])
@login_required
def get_profile():
  user = model_to_dict(current_user)
  return jsonify(data=user, status={"code": 200, "message": "Success"})


@persons.route('/register', methods=['GET', 'POST'])
def register():

  payload = request.get_json()['formData']
  print('!!!!!!!!!!!!!!!!!!!')
  print(payload)
  payload['email'].lower()

  try:
    # Does the person already exist / is the personname taken?
    models.Person.get(models.Person.email == payload['email'])
    return jsonify(data={}, status={"code": 401, "message": "A user with that email already exists."})
  except models.DoesNotExist:
    # if the person does not already exist... create a person
    payload['password'] = generate_password_hash(payload['password'])
    person = models.Person.create(**payload)

    login_user(person)

    person_dict = model_to_dict(person)

    del person_dict['password'] # Don't expose password

    return jsonify(data=person_dict, status={"code": 201, "message": "Successfully registered"})

@persons.route('/login', methods=['POST'])
def login():
  payload = request.get_json()['formData']
  payload['email'].lower()

  try:
    # see if person is registered
    person = models.Person.get(models.Person.email == payload['email'])
    person_dict = model_to_dict(person)

    # check_password_hash(hashed_pw_from_db, unhashed_pw_from_payload)
    if(check_password_hash(person_dict['password'], payload['password'])):
      del person_dict['password']
      login_user(person)
      return jsonify(data=person_dict, status={"code": 200, "message": "Success"})
    else:
      return jsonify(data={}, status={"code": 401, "message": "Email or password is incorrect"})
  except models.DoesNotExist:
    return jsonify(data={}, status={"code": 401, "message": "Email or password is incorrect"})

@persons.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    session.pop()
    session.clear()
    return jsonify(data={}, status={"code": 200, "message": "Logout Successful"})


