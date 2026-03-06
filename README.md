This project allows the transfer of playlists between accounts. The code itself is not all that special, however, having struggled with the authentication portion myself, I hope that the instructions below will be of use to someone.

It should be noted that there are other methods to accomplish this. Namely, you can share a playlist with yourself and save it on your second account. That, however, does require you to have a channel.

How to use:
1. Clone the repository.
2. Add files "source_headers.json" and "dest_headers.json"
3. Go to [https://music.youtube.com/](url).
4. Ensure that you are signed into the account you wish to copy the playlist from.
5. Open the developer console. Usually Ctrl+Shift+I, F12, or right click -> Inspect will open it.
6. Click on the network tab.
7. Click on the YouTube Music logo in the top left corner. This will reload the page and populate the netwrok tab with requests.
8. Search for a request with the name "browse?prettyPrint=false".
9. Right click the request then Copy -> Copy as cURL (bash)
10. Go to [https://curlconverter.com/](url) and paste what you copied into the textbox.
11. Scroll down to the output and where the headers start. Copy everything between the brackets including the brackets.
12. Paste what you copied into source_headers.json.
13. As is, this is not a properly formatted JSON file. So, we will fix it. First remove the hashtag near the bottom row.
14. Next, in that same row that should be labeled "cookie", go to the very end and delete the final comma.
15. Finnally, all keys and values should be surrounding in double quotes not single quotes. Open find and replace with Ctrl+F.
16. Replace all double quotes with a character that does not appear anywhere in the file such as ~ or `.
17. Next, replace all single quotes with double quotes.
18. Finally, replace your dummy character with single quotes.
19. Repeat steps 3-18 to fill in dest_headers.json as well.

Now, you can run Playlist Transferer.py.

Integrity Checker.py also exists, but I am not certain it has any use. Sometimes YouTube music may say you have fewer songs in your copied playlist. 
I built Integrity Checker.py to investigate this. As it turns out, YouTube music sometimes miscounts or perhaps has certain songs that you added are
no longer available. Either way, if you are to manually count such playlists, you will find that the amount of songs in your source account will match
that of your destination account.
