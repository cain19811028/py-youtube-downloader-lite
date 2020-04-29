import youtube_dl

def get_info(url):
    options = {
        "outtmpl" : "/mp4/%(title)s.%(ext)s"
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        video = ydl.extract_info(url, download=False)
        formats = video.get('formats')
        for f in formats:
            print("format id: %s, ext: %s, note: %s, size: %s" % (f.get("format_id"), f.get("ext"), f.get("format_note"), f.get("filesize")))

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
        "format": "bestvideo+bestaudio"
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])

"""
Main
"""
if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v="
    video_id = input("input youtube video id: ")
    option = input("1=info, 3=mp3, 4=mp4: ")

    if video_id == "":
        print("no youtube video id")
    else:
        if option == "1":
            get_info(url + video_id)
        elif option == "3":
            download_mp3(url + video_id)
        elif option == "4":
            download_mp4(url + video_id)
        print("done")