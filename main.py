from pytube import YouTube

# Create youtube object called yt
yt = YouTube("https://www.youtube.com/watch?v=PKtnafFtfEo")

yt.streams.first().download()
print(yt.captions)
print(yt.thumbnail_url)