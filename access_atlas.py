from pprint import pprint
from dotenv import find_dotenv, dotenv_values
from pymongo import MongoClient

config = dotenv_values(find_dotenv())
conn_str = config["mongodb_dev"]

client = MongoClient(conn_str)
print(client.list_database_names())

db = client["flow-backoffice"]
print(db.list_collection_names())

issuer = db.Issuer.find_one()
pprint(issuer)
