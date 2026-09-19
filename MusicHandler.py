import csv
import os
import shutil
filename = "songlist.csv"
fields = []
rows = []

base_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(base_dir, "songlist.csv")


def addSong(name,artist,album,filepath):
    try:
        # folder is in the same place as this file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        musicpath = os.path.join(base_dir, "Music")

        #make sure it exists
        os.makedirs(musicpath, exist_ok=True)

        # Yk actually move it
        dest_path = shutil.move(filepath, musicpath)
        print("File moved Yipee!")

        # put song name in the csv
        file_exists = os.path.isfile(filename)
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Name", "Artist", "Album", "Filepath"])
            writer.writerow([name, artist, album, dest_path])

    except Exception as e:
        print("didnt work:", e)
        print("the filepath is probably wrong lol")

def deleteSong(name):
    try:
        songs = []
        file_to_delete = None

        # why is this harder then addsong, finds the position of the name in the csv
        with open(filename, "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if row[0] == name:
                    file_to_delete = row[3]  # found it
                else:
                    songs.append(row)

        # make the file vanish without a trace
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(songs)

        # if the file exists, make it gone
        if file_to_delete and os.path.isfile(file_to_delete):
            os.remove(file_to_delete)
            print(f"deleted the song: {name} and removed the file {file_to_delete}")
        else:
            print(f"deleted the song: {name} unfortunately your file wasnt found.")

    except Exception as e:
        print("error deleting the song:", e)

def findSong(target):
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            header = next(reader)  # skip the first row
            for index, row in enumerate(reader, start=1):  # start=1, so the row after the header
                if row[0] == target:  # if row = the file name
                    filepath = row[3]  # we found 'em
                    return filepath, index
        # if has not been found
        return None, -1
    except Exception as e:
        print("song not found, sorry :( , ", e)
        return None, -1


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

addSong("ASGORE","Carlos Arro","ZainSongs",r"c:\Users\Lapto\Downloads\ULTRAKILL-SteamRIP.com\ULTRAKILL\Cybergrind\Music\ASGORE.mp3")