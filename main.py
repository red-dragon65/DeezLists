
import getPlaylistData as playListToFile
import comparePlaylists as playlistComparer


# Generate the playlist data for the specified user using the deezer userID
#playListToFile.getPlayListData(4063572262)


# Compare a file against another file
#playlistComparer.findDuplicates("DEZ_Aggregate", "Loved_Tracks")



# Compare a file to all files
ignoreFiles = ["Loved_Tracks",
               "DUP_Creme_de_la_creme",
               "DUP_Goated"]
playlistComparer.massCompare("DEZ_Collection", ignoreFiles)






