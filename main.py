# Main script for the audio downloaderself.

from __future__ import unicode_literals
import youtube_dl

# Path of URL List text file
path = "/home/bvandyke/proj/src/github.com/ridge-runner/tubesound/url-list.txt"

def url_fetcher(url_list_Path):
    """Reads a list of URLs from url-list.txt file and outputs a list"""

    url_list = []

    with open(path, "r") as urls:
        urls = urls.readlines()
        urls = [x.strip() for x in urls]
        url_list = urls

    del url_list[0:2] #clean up instructions on url list text file.
    #print('URLs Imported:\n\n')
    #print(url_list)
    return url_list


#formating
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(url_fetcher(path)) #takes a list of URLs

print("All done!")
