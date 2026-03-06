from ytmusicapi import YTMusic

source = YTMusic("source_headers.json")
dest = YTMusic("dest_headers.json")

sourcePlaylistId = "PLZcAfqz1eF_7wwvDf9kUzLKPSiRtUxbUD"
destPlaylistId = "PLxVeQ3F_XImyrVJ128ny72FJmJpaUp5t3"
sourcePlaylist = source.get_playlist(sourcePlaylistId, limit=None)
destPlaylist = dest.get_playlist(destPlaylistId, limit=None)

if sourcePlaylist is None or destPlaylist is None:
    if sourcePlaylist is None:
        print("Source playlist not found")
    if destPlaylist is None:
        print("Destination playlist not found")
    exit()

if len(sourcePlaylist["tracks"]) == destPlaylist["trackCount"]:
    print("Source playlist and destination playlist have the same number of tracks")
    print("Both contain", len(sourcePlaylist["tracks"]), "tracks")
    verify = input("Do you still want to see the track comparisons? (y/n): ")
    if verify.lower() not in ["yes", "y"]:
        exit()

for track in sourcePlaylist["tracks"]:
    found_track = False
    title = track["title"]
    print("Checking for ", title)
    for dest_track in destPlaylist["tracks"]:
        if dest_track["title"] == title:
            print(title, "was found in the destination playlist")
            found_track = True
            break
    if not found_track:
        print(title, "was not found in the destination playlist")
