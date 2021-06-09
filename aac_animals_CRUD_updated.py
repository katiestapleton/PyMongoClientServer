# Katie Stapleton
# CS 340
# Module 4 Milestone
# 05/29/2021

# CRUD operatations for PyMongo database
from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.errors import ConnectionFailure

class AnimalShelterCRUD(object):
    """ CRUD operations for Animal collection (only) in MongoDB """

 # initialize MongoClient and databases 
    def __init__(self, ):         
        # self.client = MongoClient('mongodb://%s:%s@localhost:51558/AAC' % ('userAdmin', 'aac')))
        self.client = MongoClient('mongodb://userAdmin:aac@localhost:39693/admin')
        self.database = self.client['AAC']
        print('connected to mongoDB')
        #raise Exception("Server is not accessible. Invalid connection and/or credentials")

# inserts document into specified database/collection
    def AddDoc(self, userData):
        """Insert one document into collection"""    
        if userData is not None:
            self.database.animals.insert(userData)  # data should be dictionary
            #result = 'Document added to the database'
            result = True
        else:
            #raise Exception("Parameter is empty. No data saved")
            result = False
        return result



# query document(s) from speficied database/collection 
    def ReadDoc(self, search): # data should be dictionary
        """Read/query collection. Requires standard key:pair syntex used for find()."""   
        if search is not None:
            result = self.database.animals.find(search)  
            return result      
        else:
            # raise Exception("Data query failed. Please check the search parameters.")
            result = 'Data query failed. Please check the search parameters. Data may not be located within the system.'
        return result