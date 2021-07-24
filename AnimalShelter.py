from pymongo import MongoClient
from pymongo import ReturnDocument


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient and database
        print ("Connecting to the MongoDB")
        self.client = MongoClient('mongodb://%s:%s@localhost:39693/?authMechanism=DEFAULT&authSource=admin' % ('userAdmin', 'aac'))
        #self.client = MongoClient(f'mongodb://{userval}:{passval}@localhost:39693/AAC')
        self.database = self.client['AAC']
        

    # Create/insert documents into database
    def create(self, data):
        """ Create/Insert data into collection """  
        # Verify that dictionary containing record data was provided, else raise an exception
        if data is not None:
            # store data into database
            insert_result = self.database.animals.insert_one(data)  # data should be dictionary

            # check if insert successful
            if insert_result.inserted_id:
                status = True
            else:
                status = False
            return status
        else:
            raise Exception("Data parameter is empty or invalid. No data saved")

    # Read/query documents from the database
    def read(self, data):
        """Read/query data in collection. Requires dictionary syntax (standard key-value pair).""" 
        # verify that search criteria is provided
        if data is not None:
            animalsCollection = self.database.animals.find(data,{"_id":False})  # data should be dictionary            
            return animalsCollection
        else:
            raise Exception("No search criteria provided")

    # Update documents from the database
    def update(self, animal, change):
        """Update data. ($set operator is needed)""" 
        # store the user values to local variables
        dataSearch = animal
        infoUpdate = change

        # Verify that update criteria was provided
        if change is not None:
            result = self.database.animals.find_one_and_update(dataSearch, infoUpdate,
                                                               return_document=ReturnDocument.AFTER)
            if result is not None:
                return result
            else:
                return ("Update failed. Please check the search parameters and try again.")
        else:
            raise Exception("No change provided")

    # Delete documents from the Database
    def delete(self, animal):
        """Delete data in collection. Requires dictionary syntax."""
        # verify deletion data was provided
        if animal is not None:
            delete_result = self.database.animals.delete_one(animal)
            return delete_result
        else:
            raise Exception("Delete failed. Please check the parameters.")

    def test(self, data):
        return data
