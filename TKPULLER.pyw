import tkinter as tk
import git 
import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
window = tk.Tk()
lbl1 = tk.Label(text="Repo to pull:")
lbl1.pack()

repoEntry = tk.Entry()
repoEntry.pack()

lbl2 = tk.Label(text="Branch:")
lbl2.pack()


branchEntry = tk.Entry()
branchEntry.pack()

lbl3 = tk.Label(text="Local path:")
lbl3.pack()

pathEntry = tk.Entry()
pathEntry.pack()


repoEntry.insert(0,config['main']['repoOrig'])
branchEntry.insert(0,config['main']['pullBranch'])
pathEntry.insert(0,config['main']['LocalPath'])
def pullRepo():
    repo_url = repoEntry.get()
    local_dir = pathEntry.get()

    if not os.path.isdir(local_dir):
        repo = git.Repo.clone_from(repo_url, local_dir) 
        repo.git.checkout(branchEntry.get())
    else:
        repo = git.Repo(local_dir)
        repo.git.checkout(branchEntry.get())
        repo.remotes.origin.pull()




importButton = tk.Button(text='PULL!', height=2, width=15, command=pullRepo)
importButton.pack()

window.mainloop()