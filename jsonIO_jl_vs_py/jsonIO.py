import json

def loadDataset(jsonFile):
    with open(jsonFile, "r") as myFile:
        dset = json.load(myFile)
    return(dset)

def saveDataset(dset, jsonFile):
    with open(jsonFile, "w") as myFile:
        json.dump(dset, myFile)
    return()
