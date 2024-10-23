import os
import shutil
a=input("Enter the path of Directory to clean\n")
def mainfunc(directory):
    os.chdir(directory)
    path=os.listdir(directory)
    for files in path:
        files1=files[-5:]
        if files1.count(".") > 0:
            n=files1.find(".")
            x=files1[(n+1):]
            x=x.upper()
            if f"{x} Files" in os.listdir(directory):
                shutil.move(files,f"{directory}\{x} Files")
            elif f"{x} Files" not in os.listdir(directory):
                os.mkdir(f"{directory}\{x} Files")
                shutil.move(files,f"{directory}\{x} Files")
        else:
            if "Folders" in os.listdir(directory):
                shutil.move(files,f"{directory}\Folders")
            elif "Folders" not in os.listdir(directory):
                os.mkdir(f"{directory}\Folders")
                shutil.move(files,f"{directory}\Folders")
mainfunc(a)