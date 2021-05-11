#importing necessary libraries

import pymongo
from pymongo import MongoClient
import datetime


class CreateAPIClass:
 
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
        if (audioFileType) is None or (audioFileId) is None:
            return False
        else :
            return True

      def checkAudioName(audioName):
        """
        Description: checks the length of audioName
        Input: audioName passed by the user
        Output: True if the length of audioName is less than 100. Else, False
        """
        if(len(audioName)>100):
            return False
        else:
            return True

      def checkAudioDuration(audioDuration):
        """
        Description: checks the duration of audio
        Input: audioDuration passed by the user
        Output: True if the value of audioDuration is less than or equal to 0. Else, False
        """
        if(audioDuration<=0):
            return False
        else:
            return True

      def checkUploadedTime(audioUploadedTime):
        """
        Description: checks the value of audioUploadedTime
        Input: audioUploadedTime generated using the datetime library
        Output: True if time is not in past. Else, False
        """
        if(audioUploadedTime != datetime.datetime.utcnow()):
           return False
        else:
            return True
    
      def checkParticipants(participant):
        """
        Description: checks the length participants names and length of participants list
        Input: List of participants passed by the user
        Output: True if the length of participant list is less than 10 and each name in list is of length less than 100. Else, False
        """
        if(not participant) or (len(participant)>10) or (any(i for i in participant if len(i) >100)):
            return False
        else:
            return True
    
      def checkLengths(audioTitle,author,narrator):
        '''
        Description: check for lengths of title , author name and narrator name
        Input: audioTitle, author and narrator passed by the user
        Output: True if the length of each argument passed is less than 100. Else, False
        '''
        if(len(audioTitle)>100) or (len(author)>100) or (len(narrator)>100):
            return False
        else:
            return True

      def insert(post):
        """
        Description: Connects the database and inserts the records
        Input: Dictionary with values passed by the user
        Output: True if entry added. Else, False
        """
        try:
            result= connectdb()
            if(result != False):
                collection.insert_one(post)
            else:
                return False
        except:
            return False
               
            
         