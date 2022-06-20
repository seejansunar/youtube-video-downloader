from pytube import YouTube
from pytube import Channel
from pytube import Playlist

# Create youtube object called yt
yt = YouTube("https://www.youtube.com/watch?v=PKtnafFtfEo")

yt.streams.first().download()
print(yt.captions)
print(yt.thumbnail_url)

c = Channel('https://www.youtube.com/c/ProgrammingKnowledge')
for url in c.video_urls[:5]:
    print(url)

p = Playlist('https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n')
for url in p.video_urls[:5]:
    print(url)