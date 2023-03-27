
import os

dataDirectory = "PlayListData/"

# Compare the first playlist against the second one
def findDuplicates(playlistFileOne, playlistFileTwo):

    # Read the data from the first file
    fileOne = open(dataDirectory + playlistFileOne, 'r')
    fileOneLines = fileOne.readlines()

    # Read the data from the second file
    fileTwo = open(dataDirectory + playlistFileTwo, 'r')
    fileTwoLines = fileTwo.readlines()

    # Compare both files
    for fileOneItem in fileOneLines:
        for fileTwoItem in fileTwoLines:

            # Separate id and title data
            formattedItemOne = fileOneItem.split(",")
            formattedItemTwo = fileTwoItem.split(",")

            # See if two of the same songs match (compare id)
            if formattedItemOne[0] == formattedItemTwo[0]:

                # Print matching data
                print("PlayList One: " + playlistFileOne)
                print("PlayList Two: " + playlistFileTwo)
                print("Duplicate found!" + formattedItemOne[1] + " ->" + formattedItemTwo[1])
                print()



# Compare the first playlist against all playlists specified
def massCompare(baseFile, ignoredFiles):

    # Get a list of all files in the PlayListData directory
    playListData = os.listdir(dataDirectory)

    # Remove the baseFile from the list
    # (we don't want to compare the playlist to itself)
    playListData.remove(baseFile)

    # Remove all ignornedFiles items
    playListData = [item for item in playListData if item not in ignoredFiles]

    # Print all duplicate items found
    print()
    for item in playListData:
        findDuplicates(baseFile, item)

