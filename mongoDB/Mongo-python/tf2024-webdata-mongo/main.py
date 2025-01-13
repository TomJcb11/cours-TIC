import pprint

from pymongo import MongoClient

# region Mongo model
client = MongoClient("localhost", 27017)
# database
db = client.get_database("Dataset")
# collection
customers = db.get_collection("restaurants")

# operation
result = customers.find_one(
    {  # what we are interested in
    },
    {  # want we want to show
        # "_id": 0,
        # "name": 1,
        # "borough": 1,
        # "address.street": 1,
        # "grades.grade": 1,
    },
)

# region exercises


response = customers.aggregate(
    [
        # Grouper par quartier et type de cuisine, et compter le nombre de restaurants pour chaque type de cuisine dans chaque quartier
        {
            "$group": {
                "_id": {"borough": "$borough", "cuisine": "$cuisine"},
                "count": {"$sum": 1},
            }
        },
        # Grouper par quartier et créer un tableau de types de cuisine avec leur nombre de restaurants
        {
            "$group": {
                "_id": "$_id.borough",
                "cuisines": {"$push": {"cuisine": "$_id.cuisine", "count": "$count"}},
            }
        },
        # Trier les types de cuisine par nombre de restaurants dans chaque quartier
        {
            "$project": {
                "cuisines": {
                    "$slice": [
                        {"$sortArray": {"input": "$cuisines", "sortBy": {"count": -1}}},
                        3,
                    ]
                }
            }
        },
    ]
)


for item in response:
    pprint.pprint(item)
