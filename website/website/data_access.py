from pymongo import MongoClient
from dateutil import parser
from datetime import datetime
from pandas import DataFrame
from bson.objectid import ObjectId
import pymongo
import re
import json

# dbname: "users_basket", "purchases", "goods"

def get_database():
    print('db connected')
    CONNECTION_STRING = "mongodb+srv://guest:guest@cluster0.2vrmo.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    return client['user_shopping_list']


def postToDatabase(obj, db="users_basket"):
    dbname = get_database()
    collection_name = dbname[db]
    now = datetime.now()
    create_date = now.strftime("%m/%d/%Y, %H:%M:%S")
    create = parser.parse(create_date)

    collection_name.insert_one(obj)


def getFromDatabase(db="users_basket"):
    dbname = get_database()
    collection_name = dbname[db]
    arr_obj = []
    item_details = collection_name.find()
    for item in item_details:
        arr_obj.append(item)
    return arr_obj


def getObjectById(object_id, db="users_basket"):
    dbname = get_database()
    collection_name = dbname[db]
    # arr_obj = []
    item = collection_name.find_one({'_id': ObjectId(object_id)})
    return item


def getAllObject( db="users_basket"):
    dbname = get_database()
    collection_name = dbname[db]
    arr_obj = []
    for x in collection_name.find({}): 
        arr_obj.append(x)
    return arr_obj


def deleteByObjectId(object_id, db="users_basket"):
    dbname = get_database()
    collection_name = dbname[db]
    result = collection_name.delete_one({'_id': ObjectId(object_id)})
    return result.deleted_count


def updateById(object_id, new_part, db="users_basket"):
    dbname = get_database()
    collection_name = dbname[db]
    result = collection_name.update_one(
        {'_id': ObjectId(object_id)}, {'$set': new_part})
    return result.matched_count


def getGoodsFromCurrentCategory(category, db="goods"):
    dbname = get_database()
    collection_name = dbname[db]
    arr_obj = []
    for x in collection_name.find({"category" : category}): 
        arr_obj.append(x)
    return arr_obj


def getFilteredItems(filter):
    dbname = get_database()
    collection_name = dbname["goods"]
    arr_obj = []
    item_details = collection_name.find(filter)
    for item in item_details:
        arr_obj.append(item)
    return arr_obj


# example of usage
if __name__ == '__main__':
    print(getFilteredItems(filter_price))
    # print(getCurrentCategory('Music&Hobby'))
#     expiry_date = '2021-07-13T00:00:00.000Z'
#     expiry = parser.parse(expiry_date)
#     item_3 = {
#     "item_name" : "Dog food",
#     "quantity" : 4,
#     "ingredients" : "food for animals",
#     "expiry_date" : expiry
#     }

    # #goods
    # item = {
    # "goods_name" : "Yamaha Pacifica PAC112JL YNS Left-Handed Electric Guitar",
    # "category" : 'Music&Hobby',
    # "subcategory" : "music",
    # "price": 800,
    # "picture_link": "https://m.media-amazon.com/images/I/31QYAWpRYfL._AC_.jpg",
    # "description": "Humbucker pickup in bridge with 2 single coils",
    # "presence": "true",
    # "expiry_date" : expiry
    # }

    # postToDatabase(item, "goods")
    #purchases
    # item_2 = {
    # "goods" : item,
    # "price": 2500,
    # "total" : 4,
    # "status" : "paid",
    # "ttn": "asdfasdf",
    # "delivery": {"country": "Ukraine", "town": "Kharkov", "street": "Astronomichnaya", "house": 25}
    # "expiry_date" : expiry
    # }
    # print(postToDatabase(item, "goods"))
