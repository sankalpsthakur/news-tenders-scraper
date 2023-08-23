#!/usr/bin/python3

import os

def CheckRepoUpdates(Debug= False):
    try:
        print(os.popen("pwd").read())
        
        status_result = os.popen("git status").read()
        if  "fatal: not a git repository " in status_result:
            print("Not a git repo")
            return "Not a Git Repo"
        if Debug: print("status is :",status_result)

        fetch_result = os.popen("git fetch").read()
        diff_result = os.popen("git diff main origin/main").read()
        if Debug:
            print("Git fetch result :" , fetch_result)
            print("Git diff result  :" , diff_result )

        if len(diff_result) == 0:
            print("Repo is up to Date")
            return
        
        else:
            pull_result=os.popen("git pull").read()
            if "updating" in pull_result.lower():
                print("Updating Latest Repo")
            else:
                for i in ["fatal","error"]:
                    if i in pull_result.lower():
                        print("ERROR: occured while Updating Repo")
                        return
            print("Repo Updated")
    
    except Exception as e:
        print("ERROR  : occured while Updating Repo | ", str(e))

if __name__ == '__main__':
    CheckRepoUpdates(Debug=False)
