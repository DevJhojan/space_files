from pymongo import MongoClient

db_clien: MongoClient

try:
  # remota: db_clien =  MongoClient('mongodb://localhost:27017/')
  db_clien = MongoClient('alñejoinvskajoejiow')
  #tambiem funciona este
  #db_clien =  MongoClient('mongodb://localhost:27017/').local # ahora se eliminan todos los ficheros que tengan local
  # code database in the nube hP9HBMYa492aYZ1i
  # password alñejoinvskajoejiow
except:
  pass