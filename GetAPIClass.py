#importing necessary libraries

import pymongo
from pymongo import MongoClient


class GetAPI:
 
    def connectdb():
        """
        Description: This function will connect the database
        Input: None
        Output: Collection point if true, else False
        """
        try:
            client = pymongo.MongoClient("mongodb://jaladhi-db:4ISgEbNmb7kQK7HhFf1yX6G67ROpYW1hb1lfP8g2n0XuFKcxeOjrcpiKJec6vmnVFJeeIuEUGZ0SgomdLabd8A==@jaladhi-db.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@jaladhi-db@")
            db = client.Audio
            collection = db['audio-files']
            return collection
        except:
            return False
   
    def validateInput(audioFileId,audioFileType):
        """
        Description: Validating if the user is passing both the required arguments
        Input: audioFileId and audioFileType as passed by the user
        Output: True if objects not null. False if one out of both the required arguments is null
        """
        if (audioFileType) is None:
            return False
        else :
            return True

    def filterbyID(audioFileId):
        """
        Description: Connects the database and filters the records
        Input: audioFileID values passed by the user
        Output: LIST of entry found and 200 Ok. Else, False
        """
        try:
            result= connectdb()
            if(result != False):
                data = collection.find(filter={"_id": audioFileId })
                return list(data) , "200 OK"
            else:
                return False
        except:
            return False

    def filterbyType(audioFileType):
        """
        Description: Connects the database and filters the records
        Input: audioFileID values passed by the user
        Output: LIST of entry found and 200 Ok. Else, False
        """
        try:
            result= connectdb()
            if(result != False):
                data = collection.find(filter={"audioFileType":audioFileType})
                return list(data) ,"200 OK" 
            else:
                return False
        except:
            return False

        

    
         