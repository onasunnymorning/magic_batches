from flask import Flask
from flask_restful import Resource, Api, reqparse
import mysql.connector
import json
from mysql.connector import Error

app = Flask(__name__)
api = Api(app)

# Setting up the DB connection
conn = mysql.connector.connect(
  host="magic_batches_db_1",
  user="root",
  passwd="thepass",
  database="mb"
)
db = conn.cursor()

parser = reqparse.RequestParser()

class ListBatches(Resource):
  def get(self):
    query = "SELECT name FROM batches"
    db.execute(query)
    result = db.fetchall()
    return result

class Batch(Resource):
  def get(self, batch_name):
    query = "SELECT name FROM batches WHERE name LIKE '%" + batch_name + "%'"
    db.execute(query)
    result = db.fetchall()
    return result

  def post(self, batch_name):
    query = "INSERT INTO batches (name) VALUES ('" + batch_name + "')"
    try:
      db.execute(query)
      conn.commit()
    except mysql.connector.Error as err:
      return str(err)
    else:
      return batch_name

api.add_resource(ListBatches, '/api/v1/listBatches/')
api.add_resource(Batch, '/api/v1/batch/<batch_name>')

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')