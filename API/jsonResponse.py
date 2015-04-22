import os
import json

def getJson (path, errorMessage):
    if ( os.path.exists(path) ):
        jsonString = open(path,"r").read()
        return json.loads(jsonString)
    else:
        return json.loads('{"error": "%s"}' % errorMessage)

def errorJson (errorMessage):
    return json.loads('{"error":"%s"}' % errorMessage)

def toJson (obj):
    return json.dumps(obj)
