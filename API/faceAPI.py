"""Python interface for the different faceAPIs"""

import unirest
import time
import os
import json
import base64

def normalize (imageURL):
    """Obtain a mugshot and features of a remote image with contain a face
       The mugshot image will be stored temporally in temp/<tempID>.jpg
       The features will be stored temporally in temp/<tempID>FEAT.json
       In succes case, the tempID will be returned [tempID > 0]
       In other case, 0 will be returned.
    """

    tempID = int(time.time()*10) #generate until 10 UID by second

    apiKey = "9179b201b48b320158fdf1a6ca8c8f92"
    apiKeyMashape = "MHVAq8DyQGmsh63UPDG3ot91qOGYp1e6xJwjsnOdbA5FuB6F6h"
    urlPost = "http://api.animetrics.com/v1/detect"
    selector = "SETPOSE"

    os.makedirs("temp/%s" % tempID)
    
    response = unirest.post("https://animetrics.p.mashape.com/detect?api_key=%s" % apiKey,
      headers={
        "X-Mashape-Key": apiKeyMashape,
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
      },
      params={
        "selector": selector,
        "url": imageURL
      }
    )

    if ( response.code == 200 ):
        fp = open("temp/%s/FEAT.json" % tempID,"w").write(json.dumps(response.body))
    else:
        return (0,"There was an error with the response of animetrics")

    try:
        setPoseUrl = response.body["images"][0]["faces"][0]["setpose_image"]
    except:
        return (0,"Face not detected")

    try:
        print("Downloading the normalize image")
        os.system("wget -q -O temp/%s/IMG.jpg %s" % (tempID,setPoseUrl))
        return (tempID,"Succes")
    except:
        return (0,"There was an error in wget")

def getAttributes (tempID, imagePath=""):
    """Obtain a the attributes (e.g. age, race) of the face in temp/tempID.jpg,or in imagePath if is specified
       The result is stored like JSON in temp/tempID/ATTR.json
    """

    if ( imagePath == "" ):
        imagePath = "temp/%s/IMG.jpg" % tempID
    
    if ( os.path.exists(imagePath) ):
        #encode the image to base64
        with open(imagePath, "rb") as imageFile:
            encodedImg = base64.b64encode(imageFile.read())

        urlPost = "http://rekognition.com/func/api/"
        apiKey = "pqbB3puEwz6xjTgW"
        apiSecret = "vJkGOOJj0j7KauSp"
        jobs = "face_detect_gender_race_age_glass_mustache_beard_beauty"

        curlString = 'curl -F "api_key=%s" -F "api_secret=%s" -F "jobs=%s" -F "base64=%s" -o "temp/%s/ATTR.json" -m 10  %s' % (apiKey,apiSecret,jobs,encodedImg,tempID,urlPost)
        print("Executing in cURL %s" % curlString)
        status = os.system(curlString)

        return (not status)
    else:
        print("The image doesn't exist")
        return 0

def faceRecognize (tempID, nameSpace = "cluster1", userID = "default", numReturn = 3, imagePath=""):
    """Search for a match against the nameSpace/userID faces
       Store the candidates list in temp/tempID/CAND.json
    """

    if ( imagePath == "" ):
        imagePath = "temp/%s/IMG.jpg" % tempID
    
    if ( os.path.exists(imagePath) ):
        #encode the image to base64
        with open(imagePath, "rb") as imageFile:
            encodedImg = base64.b64encode(imageFile.read())

        urlPost = "http://rekognition.com/func/api/"
        apiKey = "pqbB3puEwz6xjTgW"
        apiSecret = "vJkGOOJj0j7KauSp"
        jobs = "face_recognize"

        curlString = 'curl -F "api_key=%s" -F "api_secret=%s" -F "jobs=%s" -F "base64=%s" -F "name_space=%s" -F "user_id=%s" -F "num_return=%i" -o "temp/%s/CAND.json" -m 10  %s' % (apiKey,apiSecret,jobs,encodedImg,nameSpace,userID,numReturn,tempID,urlPost)
        print("Executing in cURL %s" % curlString)
        status = os.system(curlString)

        jsonMatch = json.loads(open("temp/%s/CAND.json" % tempID).read())
        candidates = jsonMatch["face_detection"][0]["matches"]

        resp = { "candidates": candidates, "tempID": tempID}

        return (not status,resp)
    else:
        print("The image doesn't exist")
        return (0,[])