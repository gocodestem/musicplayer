import csv
filename = "songlist.csv"
fields = []
rows = []




def addSong(name,artist,album,filepath):
    pass

def deleteSong(name):
    pass

def findSong(target):
    pass


def getAllSongs():
    try:
        #opens the file
        with open(filename,"r") as file:
            errorCheck = True #checks if an error has occured
            #if an error has been found then errorCheck <- False
            reader = csv.reader(file)
            fields = next(reader)
            for row in reader:
                rows.append(row)
    except StopIteration:
        errorCheck = False #to make sure the if statement below will not work
        return 0 # <- indicates that an StopIteration error occured, and that 
        #the file songlist.csv file is empty
    except :
        errorCheck = False
        return 1 # <- indicates that an unknown error occured
        #we will display a custom message using an if statement in main.py
    
    if errorCheck:
        return [[fields],[rows]]

    



getAllSongs()






