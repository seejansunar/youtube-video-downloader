from pytube import YouTube
from pytube import Channel

# Create youtube object called yt
yt = YouTube("https://www.youtube.com/watch?v=PKtnafFtfEo")

yt.streams.first().download()
print(yt.captions)
print(yt.thumbnail_url)

c = Channel('https://www.youtube.com/c/ProgrammingKnowledge')
for url in c.video_urls[:5]:
    print(url)