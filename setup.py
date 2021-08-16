import sys
import os 
import json

# Locate seems to be Being a bitch to work with so im not gonna use python to directly process the commmand

PathsArray = []
# Given that some people are highly organised within their environment they likely have a directory in which all git repos are stored the use of the condition variable allows a quick and simple usage of such
Condition = None 

os.system("locate '*/.git' > .TempCommandOutput")

if ".TempCommandOutput" in os.listdir(os.getcwd()):
    print("Processing Temporary Command File")
    with open(".TempCommandOutput","r") as f:
        lines = f.readlines()
    
    for Value in lines:
        Value = Value.strip("\n").strip(".git")
        if not Condition:
            PathsArray.append(Value)
        else:    
            # Add your Condtion Evaluation Here (E.G. "if Value.startswith('/opt/')" " 
            # ... 
            # ...
            PathsArray.append(Value)
            
    JSON = {
        "Paths" : PathsArray
    }
    
    JSON = json.dumps(JSON, indent=4)
    
    with open("Assets.json","w") as f:
        f.write(JSON)
        
    os.remove(".TempCommandOutput")
        
    
    with open(".Banned.json","w") as f:
        JSON_Banned = {
            "BannedPaths" : []
        }
        JSON_Banned = json.dumps(JSON_Banned,indent=4)
        f.write(JSON_Banned)    
    
    print("Created Assets.Json File, please manually remove any repositories which are not to be tracked")