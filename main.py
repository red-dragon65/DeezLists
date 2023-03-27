
import getPlaylistData
import comparePlaylists


# Generate the playlist data for the specified user using the deezer userID
#getPlaylistData.downloadPlayListData(4063572262)

# Compare a file against another file
#comparePlaylists.findDuplicates("DEZ_Aggregate", "Loved_Tracks")

# Compare a file to all files
ignoreFiles = ["Loved_Tracks",
               "DUP_Creme_de_la_creme",
               "DUP_Goated"]
comparePlaylists.massCompare("DEZ_Collection", ignoreFiles)






