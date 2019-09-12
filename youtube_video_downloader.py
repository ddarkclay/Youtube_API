from pytube import YouTube

link = input("Enter Youtube Video Link : ")
yt = YouTube(link)
videos = yt.streams.all()
for i,stream in enumerate(videos,1):
    print(f"{i} {stream}")

stream_number = int(input("Enter Number which want to Download : "))
video = videos[stream_number-1]
video.download("/home/sanmartin/Videos")
print("Downloaded")