from pytube import YouTube

link = input("Entre un lien Youtube : ")
yt = YouTube(link)

ys = yt.streams.get_highest_resolution()
ys.download()

print("Téléchatgemet términer")
