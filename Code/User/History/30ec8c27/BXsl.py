from pymongo import MongoClient

db_clien: MongoClient
from pymongo import MongoClient

db_clien: MongoClient

try:
  # remota: db_clien =  MongoClient('mongodb://localhost:27017/')
  # Base de datos funcionando en remoto
  db_clien = MongoClient('mongodb+srv://dev:lhiouhgiogljhh@cluster0.ecu182f.mongodb.net/')
  #tambiem funciona este
  #db_clien =  MongoClient('mongodb://localhost:27017/').local # ahora se eliminan todos los ficheros que tengan local
  # code database in the nube hP9HBMYa492aYZ1i
  # password: lhiouhgiogljhh
  # password: alñejoinvskajoejiow
except:
  print("No hizo la conección")
  
try:
  # remota: db_clien =  MongoClient('mongodb://localhost:27017/')
  # Base de datos funcionando en remoto
  db_clien = MongoClient('mongodb+srv://dev:lhiouhgiogljhh@cluster0.ecu182f.mongodb.net/')
  #tambiem funciona este
  #db_clien =  MongoClient('mongodb://localhost:27017/').local # ahora se eliminan todos los ficheros que tengan local
  # code database in the nube hP9HBMYa492aYZ1i
  # password: lhiouhgiogljhh
  # password: alñejoinvskajoejiow
except:
  print("No hizo la conección")
  