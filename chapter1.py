from pymongo import MongoClient

client = MongoClient(port=27017)

db = client.nobel
prizes_collection = db["prizes"]

filter = {}

n_prizes = db.prizes.count_documents(filter)
n_laureates = db.laureates.count_documents(filter)

print(n_prizes)
print(n_laureates)


# Save a list of names of the databases managed by client
db_names = client.list_database_names()
print(db_names)

# Save a list of names of the collections managed by the "nobel" database
nobel_coll_names = client.nobel.list_collection_names()
print(nobel_coll_names)

# Retrieve sample prize and laureate documents
prize = db.prizes.find_one()
laureate = db.laureates.find_one()

# Print the sample prize and laureate documents
print(prize)
print(laureate)
print(type(laureate))

# Get the fields present in each type of document
prize_fields = list(prize.keys())
laureate_fields = list(laureate.keys())

print(prize_fields)
print(laureate_fields)

