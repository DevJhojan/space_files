from pymongo import MongoClient

try:
  db_clien: MongoClient =  MongoClient('mongodb://localhost:27017/')
except:
  pass