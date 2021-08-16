import os 
import argparse
import json
from prettytable import PrettyTable
import logging, coloredlogs

# Create formatters
DETAILED = logging.Formatter("%(asctime)-30s %(module)-15s %(levelname)-8s %funcName)-20s %(message)s")

# Custom Logger
logger = logging.getLogger(__name__)
coloredlogs.install(logger=logger,level=logging.DEBUG)
FileHandler = logging.FileHandler("Git-MU.log")
FileHandler.setFormatter(DETAILED)
logger.addHandler(FileHandler)

Parser = argparse.ArgumentParser()
Parser.add_argument("-A",help="Automatically Update All Assets",action='store_true')

Args = Parser.parse_args()

class MuTerminal():
    
    def __init__(self,logger):
        self.logger = logger
        self.MU = "\033[1;32;40m" + "𝝁" + "\033[0m"
        self.Assets = "Assets.json" # Add Location For Assets.json here
        self.Commands = { 
                         
            "help" : {"Description" : "Get Infomation for commands (This Command)","Syntax" : "help <Command>", "Method" : self.GetHelp},
            "update-all" : {"Description" : "Update all assets", "Syntax" : "update-all", "Method" : self.UpdateAll},
            "update" : {"Description" : "update specific assets", "Syntax" : "update <Asset>", "Method" : self.Update},
            "list" : {"Description" : "List all assets from asset.json file", "Syntax" : "list", "Method" : self.ListAssets}
                         
                         }
        
    def Interactive(self):
        """
        
        """        
        while True:
            Command = input(f"{self.MU} ").lower()
            if Command.lower in ["quit","exit"]:
                quit()       
            else:
                self.RunCommand(Command)
            
    def RunCommand(self,Command):
        try:
            self.Commands.get(Command).get("Method")()
            
        except Exception as Err:
            self.logger.error(f"{Err} Detected")
            print("Command Not Recognised ; use 'help' to see a list of commands")
        
    def GetHelp(self):
        print("")
        Table = PrettyTable()
        Table.field_names = ["Command","Command Description","Syntax"]
        
        for _ in Table.field_names:
            Table.align[_] = "l"
        
        for _ in self.Commands.keys():
            CommandInfo = self.Commands.get(_)
            Table.add_row([_,CommandInfo["Description"],CommandInfo["Syntax"]])
    
        print(Table)    
        print("")
        
    def Update(self,Asset):
        print("")
        
    def UpdateAll(self):
        print("")
        
    def ListAssets(self):
        with open(self.Assets,"r") as f:
            Content = f.read()
        self.JSON = json.loads(Content)
        for _ in self.JSON["Paths"]:
            print(f"    {_}")
        
if __name__ == "__main__":
    if Args.A:
        M = MuTerminal(logger)
        M.RunCommand("update-all")
    else:
        M = MuTerminal(logger)
        M.Interactive()