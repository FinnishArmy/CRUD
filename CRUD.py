from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for the Animal collection in MongoDB"""

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 34419
        DB = 'AAC'
        COL = 'animals'
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Complete this create method to implement the C in CRUD.
    def create(self, data: dict) -> bool:
        if data is not None:
            # data should be a dictionary
            self.database.animals.insert_one(data)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Create method to implement the R in CRUD.
    def read(self, query: dict) -> list:
        # Important: Be sure to use find() instead of find_one() when developing your method. 
        # Hint: You must work with the MongoDB cursor returned by the find() method.
        cursor = self.collection.find(query or {})
        results = []
        for document in cursor:
            results.append(document)
        return results
    
    # Function to delete an entry. 
    def delete(self, query: dict) -> bool:
        #Delete documents matching the given filter.
        result = self.collection.delete_many(query)
        return result.deleted_count > 0
