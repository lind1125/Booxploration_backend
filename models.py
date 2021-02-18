from peewee import *
from flask_login import UserMixin

# establish connection with the PostGresql Database
DATABASE = PostgresqlDatabase('bookfinder_app', host='localhost', port=5432)

#refactored to be an inherited class for our models
# Model is an inherited parent Class from peewee
class BaseModel(Model):
# Linking the model to the database with class Meta
  class Meta:
    database = DATABASE

class Person(UserMixin, BaseModel):
  personname = CharField(unique=True)
  email = CharField(unique=True)
  password = CharField()

class FavedBook(BaseModel):
  person = ForeignKeyField(Person, backref='person')
  title = CharField()
  cover_url = CharField()
  apiKey = CharField()
  has_read = BooleanField()


# establish connection with the tables. If no tables exist, it will create them. safe=True guarantees that existing tables will not be overwritten.
def initialize():
  DATABASE.connect()
  DATABASE.create_tables([FavedBook, Person], safe=True)
  print("TABLES Created")
  DATABASE.close()