#importing necessary libraries

import pymongo
from pymongo import MongoClient
import datetime


class UpdateAPIClass:
 
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

      def update():
         """
         Description : updates the database
         Input: none
         Output : 200, if updated. 500, if failed
         """
         try:
            connectdb()
            updates ={'audioId':audioId}
            post = { '$set':  {"audioType":audioType,
				                "name" :audioName,
                                "duration": audioDuration,
                                "uploaded_time": datetime.datetime.utcnow()}
                     }
            collection.update_one(updates,post)
            return  "200 ok"
         except:
            return "500 :Internal Error"

         