import models 

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required


faves = Blueprint('faves', 'faves')

# route to view faved books
@faves.route('/faves', methods=['GET'])
@login_required
def get_faved_books():
    try:
        books = [model_to_dict(books) for books in \
                    models.FavedBook.select() \
                   .join_from(models.FavedBook, models.Person) \
                   .where(models.Person.id == current_user.id) \
                   .group_by(models.FavedBook.id)]
        return jsonify(data=books, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, \
                       status={"code": 401, "message": "Log in or sign up to view your faved books"})

# route to delete books from faves list
@faves.route('/faves/<book_id>', methods=['DELETE'])
@login_required
def delete_fave(book_id):
  fave_to_delete = models.FavedBook.get_by_id(book_id)
  fave_to_delete.delete_instance()
  return jsonify(data={}, status={"code": 201, "message": "Successfully deleted"})

# route to add books to faves list
# @faves.route('/faves/<book_id>', methods=['POST']) ultimately will be the urlpath
@faves.route('/addfave', methods=["POST"])
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