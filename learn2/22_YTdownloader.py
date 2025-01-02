from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title"", yt.title")

yd= yt.streams.get_highest_resolution()

yd.download("/Users/hrrniu/")

#tutaj potrzeba jeszcze troszkę pogrzebać, poczytać dokumentację pytube