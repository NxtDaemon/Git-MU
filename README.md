# Git-MU
Git Management Utility for keeping repos up to date. written in python

<p align=center>
  <img src="Git-MU_sm.png" alt="My Shitty Logo :)" >
</p>

# Recommended Implementation 
1. Use Cronjobs to run if you need bleeding-edge, use manual / periodic running via a shell spawn or something for standard usage 
2. Use git-credential manager, I dont see the point in remaking the wheel so using git-credential manager will mean private repos wont cause an issue 
3. Remove any git repos that are managed by another source, this is due to possible errors if sections of code are updated without their counterparts
4. Either ensure all repos require base user rights to update or escalate upon runtime via sudo
5. Use the `-A` flag for scripts / cronjobs 

# Commands 
```
+------------+--------------------------------------------+-------------------+
| Command    | Command Description                        | Syntax            |
+------------+--------------------------------------------+-------------------+
| help       | Get Infomation for commands (This Command) | help              |
| update-all | Update all assets                          | update-all        |
| update     | update specific assets                     | update <AssetNum> |
| list       | List all assets from asset.json file       | list              |
| asset      | Get a specific asset                       | asset <AssetNum>  |
| ban        | Add assets to a BannedList                 | ban <AssetNum>    |
| banned     | List all banned assets                     | banned            |
+------------+--------------------------------------------+-------------------+
```

# Usage Example 
```
> python3 Git-MU.py
𝝁 help

+------------+--------------------------------------------+-------------------+
| Command    | Command Description                        | Syntax            |
+------------+--------------------------------------------+-------------------+
| help       | Get Infomation for commands (This Command) | help              |
| update-all | Update all assets                          | update-all        |
| update     | update specific assets                     | update <AssetNum> |
| list       | List all assets from asset.json file       | list              |
| asset      | Get a specific asset                       | asset <AssetNum>  |
| ban        | Add assets to a BannedList                 | ban <AssetNum>    |
| banned     | List all banned assets                     | banned            |
+------------+--------------------------------------------+-------------------+

𝝁 update-all

Found 69 Already Updated Assets
Updated 0 Assets
Encountered 0 Warnings
Encountered 0 Fatal Errors
```
