import zipfile
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import json

# Path: labgrader.py

def getFileName():
    Tk().withdraw()
    filename = askopenfilename()
    return filename

def unzipCore(filename):
    zip_ref = zipfile.ZipFile(filename, 'r')
    zip_ref.extractall()
    zip_ref.close()

def unzipStudent(file):
    zFile = zipfile.ZipFile(file, 'r')
    zFile.extractall()
    extracted = zFile.namelist()
    for pyfile in extracted:
        if pyfile.endswith(".py"):
            os.rename(pyfile, file.split("_")[0] + ".py")
            print("Renamed " + extracted[0] + " to " + file.split(".")[0] + ".py")
        else:
            os.remove(pyfile)
    zFile.close()
    os.remove(file)


def commentOut(grade):
    print(os.listdir())
    for file in os.listdir():
        if file != "labgrader.py":
            comments = []
            with open(file, "r") as f:
                for line in f:
                    if '#' in line:
                        comments.append('#' + line.split('#')[1])
                    else:
                        continue
            grade[file] = comments
            os.remove(file)
    return grade

            
def main():
    filename = getFileName()
    unzipCore(filename)
    for file in os.listdir():
        if file.endswith(".zip"):
            unzipStudent(file)
    grade = {}
    commentOut(grade)
    cleandata = json.dumps(grade, indent=10)
    print(cleandata)
    print("Done!")

if __name__ == "__main__":
    main()