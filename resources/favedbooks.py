import models 

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required


faves = Blueprint('faves', 'faves')

# route to view faved books
@faves.route('/faves', methods=['GET'])

# route to add books to faves list
@faves.route('/faves/<book_id>', methods=['POST'])

# route to delete books from faves list
@faves.route('/faves/<book_id>', methods=['DELETE'])


@faves.route('/add', methods=["POST"])
@login_required
def create_fave():
   # create the fave w/ payload info if current_user exists
    # if current_user.id:
      payload = request.get_json()
      print('!!!!!!!!!!!!!!!!!!!')
      print(payload)
      fave = models.FavedBook.create(person=current_user.id, **payload)
      fave_dict = model_to_dict(fave)

      return jsonify(data=fave_dict, status={"code": 201, "message": "Success"})