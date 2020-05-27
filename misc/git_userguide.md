This section presents several useful git commands that you may encounter in a daily basis.

### Creating branch 

#### Creating branch from the master branch

    git checkout -b <name-of-branch>
    
For example:

    git checkout -b dev/feature_x

#### Creating sub-branch from another branch

    git checkout -b sub_branch father_branch
    
For example:

    git checkout -b dev/feature_x dev


### Checking for update
  
    git status

If you need a stronger checking on all branches, use:

    git fetch   


### Pulling

    git pull
    
A more specific (and stronger) pulling:

    git pull <remote> <name-of-branch>               

For example:

    git pull origin dev


### Adding changes to commit

#### Adding all files to a buffer:

    git add .

or a specific file:

    git add <file_name>

#### Generate a commit request with a clear message:

    git commit -m "message"

### Pushing

Pushing files to git repositorie:

    git push <remote> <name-of-branch> 

For example:

    git push origin dev 

A stronger pushing when you have some conflicts with the online version of the codes, use this only when you know what you are doing: 

    git push --force <remote> <name-of-branch>      


### Miscellaneous

#### Switching to a branch 

    git checkout <name-of-branch>


#### Renaming a branch

    git branch -m <name-of-branch> <new-name-of-branch>

#### Deleting a branch

    git branch -d <name-of-branch-to-delete>

#### Removing uncommitted changes

For tracked files:

    git checkout -f              

For untracked files:

    git clean -fd  

Or undo the staged files:          

    git reset HEAD               
