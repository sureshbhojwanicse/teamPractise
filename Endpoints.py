#importing necessary libraries and user defined classes for different endpoints
import pymongo
import datetime
import GetAPIClass
import DeleteAPIClass
import UpdateAPIClass
import CreateAPIClass
from typing import Dict
from fastapi import FastAPI,Request

#initializing fastapi
app = FastAPI()

@app.get("/get/")
def get_api(json_data: Dict):
    """
    Description: This Function will fetch the details based on user input. 'audioFileType' is a compulsory input to be given
    Input: User input in the form of dictionary
    Output: 400, if the request is bad (input not proper). 200, if record returned.
    """
    #taking json input in local variables
    audioFileId = json_data.get('audioFileID')
    audioFileType = json_data.get('audioFileType')

    #creating object of GetAPIClass which has db connections and validating input functions
    g = GetAPIClass()

    if (g.validateInput(audioFileId,audioFileType) == False):
        return {"The request is invalid: 400 bad request"}
    else:
        #filtering based in audioFileId
        if audioFileId is not None:
            g.filterbyID(audioFileId)
        #filtering based on audioFileType
        else:
            g.filterbyType(audioFileType)
        return {"The request is invalid: 400 bad request"}

@app.delete("/delete/")
def delete_api(json_data: Dict):
    """
    Description:This function will delete the document based on the user input
    Input: User input in the form of dictionary
    Output: 400, if the request is bad (input not proper). 200, if record inserted. 500, if record fails to be deleted
    """
    audioFileID = json_data.get('audioFileID')
    #initializing the class object
    d= DeleteAPIClass()
    #checking if id is null
    if d.validateInput(audioFileID) == False:
        return {"The request is invalid: 400 bad request"}
    else:
        #filtering based on the input. The output is the cursor
        audio_obj = collection.find(filter={"_id":audioFileID})
        #converting the cursor object into list
        audio_list =list(audio_obj)
        #checking if any entry based on input is found or not
        if (d.checkList(audio_list) == False):
            return {"The request is invalid: 400 bad request"}
            #deleting based on the user input
        else:
            try:
                d.delete(audioFileID)
                return {"status":"200 ok"}
            except:
                return {"status":"500 Internal Error"}
            

@app.post("/create/")
def create_api(json_data: Dict):
    """
    Description: This function inserts records in the document "audio-files
    Input: User input in the form of dictionary
    Output: 400, if the request is bad (input not proper). 200, if record inserted. 500, if record fails to be inserted
    """

    #taking audioFileType in local variable
    audioType = json_data.get('audioFileType')

    #creating object of the class
    c = CreateAPIClass()

    #checking if audioType is not passed by the user
    if audioType is None:
        return {"The request is invalid: 400 bad request"}
   
    #checking if the type is song and checking the input passed by the user
    if (audioType =="song"):
        audioId = json_data.get('audioId')
        audioDuration = json_data.get('audioDuration')
        audioUploadedTime = datetime.datetime.utcnow()
        audioName = json_data.get('audioName')
        if (c.checkAudioName(audioName) ==False) or (c.checkAudioDuration(audioDuration)==False) or (c.checkUploadedTime(audioUploadedTime)== False):
            return {"The request is invalid: 400 bad request"}
        else:
            #inserting the values in document
            post = { "_id": audioId,
		               "audioFileType": "song",
                      "name" :audioName,
                      "duration": audioDuration,
                      "uploaded_time": datetime.datetime.utcnow()
                     }
            try:
               c.insert(post)
               return  {"status":"200 ok"}
            except:
                return {"status":"500 Internal Error"}
       
    #checking if the type is podcast and checking the inputs passed by the user
    if (audioType == "podcast"):
        audioId = json_data.get('audioId')
        audioDuration = json_data.get('audioDuration')
        audioUploadedTime = datetime.datetime.utcnow()
        audioHost = json_data.get('audioHost')
        audioName = json_data.get('audioName')
        participant= json_data.get('participants')
        if (c.checkParticipants(participant)==False) or (checkAudioDuration(audioDuration)==False) or (checkUploadedTime(audioUploadedTime)== False):
            return {"The request is invalid": "400 bad request"}
        else:
            #inserting the values in document
            post = {"_id":audioId,
                      "audioFileType": "Podcast",
                      "audioHost": audioHost,
                      "name" :audioName,
                      "duration": audioDuration,
                      "participants": participant,
                      "uploaded_time": datetime.datetime.utcnow()
                     }
            try:
                c.insert(post)
                return {"status":"200 ok"}
            except:
                return {"status":"500 Internal Error"}

        #checking if the type id audiobook and checking the inputs passed by the user
        if (audioType =="audiobook"):
            audioId = json_data.get('audioId')
            audioDuration = json_data.get('audioDuration')
            audioUploadedTime = datetime.datetime.utcnow()
            audioTitle = json_data.get('audioTitle')
            author = json_data.get("audioAuthor",None)
            narrator = json_data.get("audioNarrator",None)
            
            if (c.checkLengths(audioTitle,author,narrator)== False) or (c.checkAudioDuration(audioDuration)== False) or (c.checkUploadedTime(audioUploadedTime)== False):
               return {"The request is invalid":" 400 bad request"}
            else:
               #inserting the values in document
                post = {"_id":audioId,
                      "audioFileType": "audiobook",
                      "title": audioTitle,
                      "duration": audioDuration,
                      "narrator": narrator,
                      "author": author,
                      "uploaded_time": datetime.datetime.utcnow()
                     }
                try:
                    c.insert(post)
                    return {"status":"200 ok"}
                except:
                    return {"status":"500 Internal Error"}

@app.put("/update/")
def update_api(json_data: Dict):
    """
    Description :This function will update the entries in the document
    Input: User input in the form of dictionary
    Output: 400, if the request is bad (input not proper). 200, if record updated. 500, if record fails to be updated
    """
    #taking user input in local variables
    audioType = json_data.get('audioFileType')
    audioId = json_data.get('audioFileID')

    #creating a class object
    u = UpdateAPIClass()

    if u.validateInput(audioId,audioType) == False:
        return {"The request is invalid": "400 bad request"}
    else :
        #saving other details in local variables
        audioId = json_data.get('audioId')
        audioDuration = json_data.get('audioDuration')
        audioUploadedTime = datetime.datetime.utcnow()
        audioName = json_data.get('audioName')
        #validating the input
        if (u.checkAudioName(audioName)== False) or (u.checkUploadedTime(audioUploadedTime)== False) or (u.checkAudioDuration(audioDuration)== False):
            return {"The request is invalid": "400 bad request"}
        else:
            #performing update query
            u.update()


