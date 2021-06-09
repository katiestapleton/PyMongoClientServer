# Katie Stapleton
# CS 340
# Module 4 Milestone
# 05/29/2021

# Pytest for custom CRUD method created for AAC.animals database


# from pymongo import MongoClient
# from bson.objectid import ObjectId
from aac_animals_CRUD_updated import AnimalShelterCRUD

# REQUIRES PYTEST
# look into using fixtures later
class TestAnimalShelterCRUD:
    
    run =  AnimalShelterCRUD()

#***********************************
# TEST WITH NO DATA ()
    # userData = None
    # search = None

# TEST WITH BLANK DATA ()
    # userData = {}
    # search = None
    
# TEST WITH SAMPLE DATA    
    # mockup document/data for testing
    userData = {
        "age_upon_outcome" : "3 years",
        "animal_id" : "TEST001",
        "animal_type" : "Test breed",
        "breed" : "Test Cat Mix",
        "color" : "Test Color Black",
        "date_of_birth" : "2014-04-10",
        "datetime" : "2017-04-11 09:00:00",
        "monthyear" : "2017-04-11T09:00:00",
        "name" : "Complex name",
        "outcome_subtype"  : "SCRP",
        "outcome_type" : "Transfer",
        "sex_upon_outcome" : "Neutered Male",
        "location_lat" : 35.625439455,
        "location_long" : -96.3435972102188,
        "age_upon_outcome_in_weeks"  : 156.767857142857
    }
    
    search = {"breed" : "Beagle"}
    
    
    # test create/upload function
    addData = run.AddDoc(userData)
    print(addData)

    # Test read/find() function
    findData =  run.ReadDoc(search)
    print(findData)
