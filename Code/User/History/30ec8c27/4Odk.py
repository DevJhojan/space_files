from pymongo import MongoClient

db_clien: MongoClient

try:
  db_clien =  MongoClient('mongodb://localhost:27017/')
  #tambiem funciona este
  #db_clien =  MongoClient('mongodb://localhost:27017/').local # ahora se eliminan todos los ficheros que tengan local
except:
  pass