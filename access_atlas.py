from pymongo import MongoClient

conn_str = ""
client = MongoClient(conn_str)

print(client.list_database_names())

backoffice_db = client["backoffice"]
print(backoffice_db.list_collection_names())

issuer = backoffice_db.Issuer.find_one()
print(issuer)
