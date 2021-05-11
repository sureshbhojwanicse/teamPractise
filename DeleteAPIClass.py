#importing necessary libraries

import pymongo
from pymongo import MongoClient


class DeleteAPIClass:

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

   
    def validateInput(audioFileID):
        """
        Description:Validating if the user is passing required arguments
        Input: audioFileID passed by the user
        Output: True if the audioFileID is not empty, else False
        """
        if (audioFileID) is None:
            return False
        else :
            return True

    def checkList(audio_list):
        """
        Description :Checking if cursor's value list is empty
        Input: audio_list which is obtained by converting the cursor into list
        Output: Returns True if the list is not empty, else False
        """  
        if(audio_list ==[]):
            return False
        else:
            return True

    def delete(audioFileID):
        """
        Description: Connects the database and deletes the entry from the document "audio-files" based on audioFileID
        Input: audioFileID passed by the user
        Output: True if entry deleted. False if the collection not found or entry not found
        """
        try:
            result =connectdb()
            if(result !=False):
              collection.delete_one(filter={"_id": audioFileID})
            else:
              return False
        except:
              return False
      

         