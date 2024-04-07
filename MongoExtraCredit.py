
from pymongo import MongoClient
# 1. Create mongodb operation objects
# 2. Call find with the operand to get the result
# 3. for walking through the printout
# 4. close the operand

# Connect to the local MongoDB
client = MongoClient("127.0.0.1", 27017)
# Selective database
db = client["airbnb"]
collection = db['listings']

# Query condition
query = {
    "neighbourhood": "Barcelona, Spain",
    "beds": {"$gt": 2}
}
# Control display
projection = {
    "_id": 0,
    "name": 1,
    "beds": 1,
    "review_scores_rating": 1,
    "price": 1
}

# Recreate analyses query
result = collection.find(query, projection).sort("review_scores_rating", -1)
for result in result:
    print(result)

# Close operand
client.close()
