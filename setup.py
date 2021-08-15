import sys
import os 
import json

# Locate seems to be Being a bitch to work with so im not gonna use python to directly process the commmand

PathsArray = []


os.system("locate '*/.git' > .TempCommandOutput")

if ".TempCommandOutput" in os.listdir(os.getcwd()):
    print("Processing Temporary Command File")
    with open(".TempCommandOutput","r") as f:
        lines = f.readlines()
    
    for Value in lines:
        PathsArray.append(Value.strip("\n").strip(".git"))
        
    JSON = {
        "Paths" : PathsArray
    }
    
    JSON = json.dumps(JSON, indent=4)
    
    with open("Assets.Json","w") as f:
        f.write(JSON)
        
    os.remove(".TempCommandOutput")
        
    print("Created Assets.Json File, please manually remove any repositories which are not to be tracked")