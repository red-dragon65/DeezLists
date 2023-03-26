
# Use deezer-python library
import deezer

# For creating data directory
import os

# For removing special chars in file name
import re

# Specify data directory
dataDirectory = "PlayListData"

# Setup client for making requests
client = deezer.Client()


### Download the specified users playlist data
def getPlayListData(publicUserID):
    print()

    # Get specified user object
    publicDeezerUser = client.get_user(publicUserID)

    # List user names
    print("Deezer Profile Name:")
    print(publicDeezerUser)
    print()

    # Get users public playlists
    usersPublicPlaylists = publicDeezerUser.get_playlists()

    # Print name of all playlists found
    print("Playlists found:")
    for playlist in usersPublicPlaylists:
        print(playlist.title)
    print()

    # Create directory to hold playlist data
    # Continue if new directory is created
    # Stop if directory already exists
    if not _createDirectory():
        print("Data already exists!")
        print("Remove directory '" + dataDirectory + "' to re-download data!")
        return

    # Loop through each song in each playlist and save to file
    for playlist in usersPublicPlaylists:

        # Format the playlist title
        # (No special characters)
        # (Replace space with underscore)
        formattedTitle = re.sub(r'\W+', ' ', playlist.title)
        formattedTitle = re.sub(r'\s+', '_', formattedTitle)

        # Create file (append mode)
        playlistFile = open(dataDirectory + "/" + formattedTitle, "a")
        print("\nCreating file: " + playlist.title)

        # Write the song data to the file
        for song in playlist.get_tracks():
            playlistFile.write(str(song.id) + ", " + song.title + ", " + song.artist.name + "\n")
            print(".", end="")

    print()



# Create a directory to hold the playlist data
def _createDirectory():
    isExist = os.path.exists(dataDirectory)

    if not isExist:
        os.makedirs(dataDirectory)
        return True
    else:
        return False
