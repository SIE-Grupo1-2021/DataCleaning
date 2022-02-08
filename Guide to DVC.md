# Guide to DVC
## Initial setup

1. Download DVC [here](https://dvc.org/)
2. Write in a text file the root location of this repository. This will be needed every time you "save" changes. 
3. Open the terminal. 
4. Change directory to the root location of this repository, i.e. cd location. 
5. As in Git, you want to "download" the new items and changes in the repository by typing: 

```console
user@machine:~$ dvc pull
```
6. 
   1. The first time, it'll ask you to authenticate with your Google account. Highlight and go to the link by right clicking and selecting the go option. 
   2. Give necessary permissions. 
   3. Copy and paste the authentication code in the terminal. 
   4. You're set to go.  

## Usual steps

1. **ALWAYS** pull first in Github Desktop to retrieve any changes. 
2. Do steps 2-5 from [Initial Setup](#initial-setup). 
3. Work on the data file. 
4. Save changes by doing a commit. 
```console
user@machine:~$ dvc commit
```
5. Push changes to Google Drive. 
```console
user@machine:~$ dvc push
```
6. Commit and push as usual using Github Desktop. 
7. You're done!

## Advice
Please always alert when working. Changes can't overlap using Excel. Do frequent commits and have backups in other locations. 