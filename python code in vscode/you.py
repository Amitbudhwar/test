from pytube import YouTube
link = "https://youtu.be/lnMi9hkMkqY"
yt = Youtube(link)
yt.streams.first().download()

















