#! /bin/bash

function create(){
    cd ~
    python3 /Users/aashi/desktop/projects/shell_script_automation/create.py $1
    cd /Users/aashi/desktop/projects/$1
    echo $1 >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/Aashi-001/$1.git
    git push -u origin main
    code .
}

#source /Users/aashi/desktop/projects/shell_script_automation/.my_commands.sh