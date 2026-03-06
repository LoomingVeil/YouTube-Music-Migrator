from ytmusicapi import YTMusic

source = YTMusic("source_headers.json")
dest = YTMusic("dest_headers.json")

playlists = source.get_library_playlists()
print("Found", len(playlists), "playlists")
for p in playlists:
    title = p["title"]
    print("Copying", title+"...")

    tracks = source.get_playlist(p["playlistId"], limit=None)["tracks"]

    new_id = dest.create_playlist(title, "Copied playlist")

    video_ids = [t["videoId"] for t in tracks if t["videoId"]]

    dest.add_playlist_items(new_id, video_ids)