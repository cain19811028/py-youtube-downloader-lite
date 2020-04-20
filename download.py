import youtube_dl

def download_mp3(url):
    options = {
        "outtmpl" : "/mp3/%(title)s.%(ext)s",
        "format"  : "bestaudio/best",
        "postprocessors": [{
            "key" : "FFmpegExtractAudio",
            "preferredcodec"   : "mp3",
            "preferredquality" : "320"
        }]
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])

def download_mp4(url):
    options = {
        "outtmpl" : "/mp4/%(title)s.%(ext)s",
        "format"  : "bestvideo/best"
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])

"""
Main
"""
if __name__ == "__main__":
	url = "https://www.youtube.com/watch?v="
	video_id = input("input youtube video id:")
	option = "mp4"

	if(video_id == ""):
	    print("no youtube video id")
	else:
	    if(option == "mp3"):
	        download_mp3(url + video_id);
	    else:
	        download_mp4(url + video_id);
	    print("done")