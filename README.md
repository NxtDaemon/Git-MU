# Git-MU
Git Management Utility for keeping repos up to date.

<p align=center>
  <img src="Git-Mu.png" alt="My Shitty Logo :)" >
</p>

# Recommended Implementation 
1. Use Cronjobs to run if you need bleeding-edge, use manual / periodic running via a shell spawn or something for standard usage 
2. use git-credential manager, I dont see the point in remaking the wheel so using git-credential manager will mean private repos wont cause an issue 
3. remove any git repos that are managed by another source, this is due to possible errors if sections of code are updated without their counterparts
4. Either ensure all repos require base user rights to update or escalate upon runtime via sudo
