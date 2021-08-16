import os 
import subprocess 
import argparse
import json
from prettytable import PrettyTable
import logging, coloredlogs
import requests

# Written By NxtDaemon Any Issues or Additions you would like please contact me here https://nxtdaemon.xyz/contact
#  __    __            __     _______                                                   
# |  \  |  \          |  \   |       \                                                  
# | ▓▓\ | ▓▓__    __ _| ▓▓_  | ▓▓▓▓▓▓▓\ ______   ______  ______ ____   ______  _______  
# | ▓▓▓\| ▓▓  \  /  \   ▓▓ \ | ▓▓  | ▓▓|      \ /      \|      \    \ /      \|       \ 
# | ▓▓▓▓\ ▓▓\▓▓\/  ▓▓\▓▓▓▓▓▓ | ▓▓  | ▓▓ \▓▓▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓▓▓▓▓\▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓▓▓▓▓▓\
# | ▓▓\▓▓ ▓▓ >▓▓  ▓▓  | ▓▓ __| ▓▓  | ▓▓/      ▓▓ ▓▓    ▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓  | ▓▓ ▓▓  | ▓▓
# | ▓▓ \▓▓▓▓/  ▓▓▓▓\  | ▓▓|  \ ▓▓__/ ▓▓  ▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓__/ ▓▓ ▓▓  | ▓▓
# | ▓▓  \▓▓▓  ▓▓ \▓▓\  \▓▓  ▓▓ ▓▓    ▓▓\▓▓    ▓▓\▓▓     \ ▓▓ | ▓▓ | ▓▓\▓▓    ▓▓ ▓▓  | ▓▓ 
#  \▓▓   \▓▓\▓▓   \▓▓   \▓▓▓▓ \▓▓▓▓▓▓▓  \▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓\▓▓  \▓▓  \▓▓ \▓▓▓▓▓▓ \▓▓   \▓▓

# Create formatters
DETAILED = logging.Formatter("%(asctime)-30s %(module)-15s %(levelname)-8s %funcName)-20s %(message)s")

# Custom Logger
logger = logging.getLogger(__name__)
coloredlogs.install(logger=logger,level=logging.DEBUG) # Change this for Debugging

# Argparse for easy scripting
Parser = argparse.ArgumentParser()
Parser.add_argument("-A",help="Automatically Update All Assets",action='store_true')
Args = Parser.parse_args()

class MuTerminal():
    
    def __init__(self,logger):
        self.logger = logger
        self.AbsPath = "/home/nxtdaemon/Git-MU/" # Assing this yourself
        self.MU = "\033[1;32;40m" + "𝝁" + "\033[0m"
        self.Assets = "Assets.json" # Add Location For Assets.json here
        self.SetupAssets()
        self.Commands = { 
                         
            "help" : {"Description" : "Get Infomation for commands (This Command)","Syntax" : "help", "Method" : self.GetHelp, "Positional" : False},
            "update-all" : {"Description" : "Update all assets", "Syntax" : "update-all", "Method" : self.UpdateAll, "Positional" : False},
            "update" : {"Description" : "update specific assets", "Syntax" : "update <AssetNum>", "Method" : self.Update, "Positional" : True},
            "list" : {"Description" : "List all assets from asset.json file", "Syntax" : "list", "Method" : self.ListAssets,"Positional" : False},
            "asset" : {"Description" : "Get a specific asset", "Syntax" : "asset <AssetNum>", "Method" : self.GetAsset,"Positional" : True},
            "ban" : {"Description" : "Add assets to a BannedList", "Syntax" : "ban <AssetNum>", "Method" : self.BannedList,"Positional" : True},
            "banned" : {"Description" : "List all banned assets", "Syntax" : "banned", "Method" : self.Banned,"Positional" : False}

            

                         }
        
        
    def Interactive(self):
        """
        
        """        
        while True:
            CommandInput = input(f"{self.MU} ").lower().split(" ")
            if CommandInput[0] in ["quit","exit","q"]:
                quit()       
            else:
                Command = CommandInput[0]
                CommandInput.pop(0)
                Args = CommandInput
                self.RunCommand(Command,Args)
            
    def RunCommand(self,Command,Args):
        try:
            print("")
            if Args:
                self.Commands.get(Command).get("Method")(Args)
            else:
                if self.Commands[Command]["Positional"] and not Args:
                    print(f"Missing Argument for {Command}")
                    print("")
                    return()
                else: 
                    self.Commands.get(Command).get("Method")()
            print("")
            
        except Exception as Err:
            self.logger.debug(f"{Err} Detected")
            print("Command Not Recognised ; use 'help' to see a list of commands")
        
    def GetHelp(self):
        Table = PrettyTable()
        Table.field_names = ["Command","Command Description","Syntax"]
        
        for _ in Table.field_names:
            Table.align[_] = "l"
        
        for _ in self.Commands.keys():
            CommandInfo = self.Commands.get(_)
            Table.add_row([_,CommandInfo["Description"],CommandInfo["Syntax"]])
    
        print(Table)    
        
    def Update(self,AssetNum):
        AssetNum = int(AssetNum[0]) - 1
        try: 
            Asset = self.Paths[AssetNum]
            Output = subprocess.Popen(f"git -C {Asset} pull --allow-unrelated-histories".split(" "),stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            StdOut = Output[0].decode().strip()
            StdErr = Output[1].decode().strip()
            if StdOut == "Already up to date.":
                print(f"{list(reversed(Asset.split('/')))[1]} is Already up to date")
            if "warning" in StdErr.lower():
                logger.warning(StdErr.strip("warning:"))
            elif "fatal" in StdErr.lower() or "error" in StdErr.lower():
                logger.error(StdErr.strip("fatal:").strip("error:"))
            else: 
                print(f"{list(reversed(Asset.split('/')))[1]} Updated")
        
        except IndexError as Exc:
            print(f"It Appears Asset At {AssetNum + 1} Does Not Exist")
            
        except Exception as Exc:
            logger.debug(f"{Exc} Occured")

    def UpdateAll(self):
        c = w = f = Au = 0 
        for Asset in self.Paths:
            if Asset in self.BannedPaths:
                logger.debug(f"{Asset} Observed Banned; No further action")
            else:
                try: 
                    Output = subprocess.Popen(f"git -C {Asset} pull --allow-unrelated-histories".split(" "),stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
                    StdOut = Output[0].decode().strip()
                    StdErr = Output[1].decode().strip()
                                        
                    if StdOut == "Already up to date.":
                        Au += 1
                        logger.info(f"Output '{Output}' for {Asset}")
                        logger.debug(f"{list(reversed(Asset.split('/')))[1]} is Already up to date")
                        continue
                             
                    if "warning" in StdErr.lower():
                        logger.warning(f"{StdErr.strip('warning:')} | {Asset}")
                        w += 1 
                        c += 1
                        continue
                    
                    elif "fatal" in StdErr.lower() or "error" in StdErr.lower():
                        logger.error(f"{StdErr.strip('fatal:').strip('error:')} | {Asset}")
                        f += 1
                        continue
                    
                     
                    print(f"\033[1;32;40m{list(reversed(Asset.split('/')))[1]}\033[0m Updated")
                    c += 1

                         
                except Exception as Exc:
                    logger.debug(f"{Exc} Occured")
                    pass
        
        print(f"Found \033[1;34;40m{Au}\033[0m Already Updated Assets")        
        print(f"Updated \033[1;32;40m{c}\033[0m Assets")        
        print(f"Encountered \033[1;33;40m{w}\033[0m Warnings")
        print(f"Encountered \033[1;31;40m{f}\033[0m Fatal Errors")

    def SetupAssets(self):    
        if self.Assets in os.listdir(self.AbsPath):
            with open(f"{self.AbsPath}{self.Assets}","r") as f:
                Content = f.read()
            self.Paths = json.loads(Content)["Paths"]
        else: 
            logger.ERROR(f"{self.Assets} Cannot be found.")
            
        if ".Banned.json" in os.listdir(self.AbsPath):
            with open(f"{self.AbsPath}.Banned.json") as f:  
                content = f.read()
            self.BannedPaths = json.loads(content)["BannedPaths"]
        else:
            logger.error(f"{self.AbsPath}.Banned.json cannot be found, have you ran setup.py?")
        
    
        
    def ListAssets(self):
        for _ in enumerate(self.Paths,start=1):
            c = _[0]
            _ = _[1]
            print(f"\033[1;32;40m   {str(c).zfill(2)} \033[0;34m{_}\033[0m")
            
    def GetAsset(self,AssetNum):
        try:
            AssetNum = int(AssetNum[0]) - 1
            print(f"\033[1;32;40m   {str(AssetNum).zfill(2)} \033[0;34m{self.Paths[AssetNum]}\033[0m")
        
        except IndexError as Exc:
            print(f"It Appears Asset At {AssetNum + 1} Does Not Exist")
    
    
    def BannedList(self,AssetNum):
        try:
            AssetNum = int(AssetNum[0]) -1

            BannedPaths = self.BannedPaths
            Path = self.Paths[AssetNum]
            if Path in BannedPaths:
                print("Path is Already in BannedList")
                return()
            
            BannedPaths.append(Path)
            BannedArray = {
                "BannedPaths" : BannedPaths
            }
            self.UpdateBanList(BannedArray)
            print(f"Added \033[1;34;40m{Path}\033[0m to BannedList")
        except IndexError as Exc:
            print(f"It Appears Asset At {AssetNum + 1} Does Not Exist")


    def UpdateBanList(self,BannedArray):
        with open(".Banned.json","w") as f:
            JSON_Banned = json.dumps(BannedArray,indent=4)
            f.write(JSON_Banned)       
        
    def Banned(self):
        if len(self.BannedPaths) == 0:
            print("There are Currently No Banned Paths")
        else:
            for _ in self.BannedPaths:
                print(f"\033[1;32;40m   {self.Paths.index(_)} \033[0;34m{_}\033[0m")

if __name__ == "__main__":
    if Args.A:
        M = MuTerminal(logger)
        M.RunCommand("update-all",[])
    else:
        M = MuTerminal(logger)
        M.Interactive()