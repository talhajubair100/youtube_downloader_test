from pytube import YouTube


link = input("Enter The Video Link Here: ")
yt = YouTube(link)


#Title of video
print("Video Title:" ,yt.title)
#Number of views of video
print("Number of views: ",yt.views)
#Length of the video
print("Length of the video: ",yt.length,"seconds")
#Description of video
print("Description of the video: ",yt.description)
#Rating
print("Ratings of the video: ",yt.rating)
#printing all the available streams
#print(yt.streams)
#print(yt.streams.filter(only_audio=True))
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")
