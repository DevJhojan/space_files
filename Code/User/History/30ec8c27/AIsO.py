from pymongo import MongoClient

db_clien: MongoClient

try:
  # remota: db_clien =  MongoClient('mongodb://localhost:27017/')
  # Base de datos funcionando en remoto
  db_clien = MongoClient('mongodb+srv://Dev:alñejoinvskajoejiow@jhojan.e611l30.mongodb.net/?retryWrites=true&w=majority')
  #tambiem funciona este
  #db_clien =  MongoClient('mongodb://localhost:27017/').local # ahora se eliminan todos los ficheros que tengan local
  # code database in the nube hP9HBMYa492aYZ1i
  # password: alñejoinvskajoejiow
except:
  pass