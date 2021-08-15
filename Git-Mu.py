import os 
import logging 
import argparse
import json

Parser = argparse.ArgumentParser()
Parser.add_argument("-A",help="Automatically Update All Assets",action='store_true')

Args = Parser.parse_args()

class MuTerminal():
    
    def __init__(self):
        self.MU = "𝝁"
        self.Assets = "" # Add Location For Assets.json here
        self.Commands = { 
                         
            "help" : {"Description" : "Get Infomation for commands (This Command)","Syntax" : "help <Command>", "Method" : self.GetHelp},
            "update-all" : {"Description" : "Update all assets", "Syntax" : "update-all"},
            "update" : {"Description" : "update specific assets", "Syntax" : "update <Asset>"},
            "list" : {"Description" : "List all assets from asset.json file", "Syntax" : "list"}
                         
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
        except KeyError:
            print("Command Not Recognised")
        
        
    def GetHelp(self):
        print("")
        for _ in self.Commands.keys():
            CommandInfo = self.Commands.get(_)
            print(f"{_.ljust(len(max(self.Commands)))} | {CommandInfo['Description']} | {CommandInfo['Syntax']}")    
        print("")
        
    # def Update(self,Asset)

        
if __name__ == "__main__":
    if Args.A:
        M = MuTerminal()
        M.RunCommand("update-all")
    else:
        M = MuTerminal()
        M.Interactive()