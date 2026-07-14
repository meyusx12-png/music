from yt_dlp import YoutubeDL

YDL_OPTIONS = {
    "format": "bestaudio/best",
    "quiet": True,
    "noplaylist": True,
}

def youtube_bul(sorgu):
    with YoutubeDL(YDL_OPTIONS) as ydl:
        bilgi = ydl.extract_info(f"ytsearch:{sorgu}", download=False)
        video = bilgi["entries"][0]

        return {
            "baslik": video["title"],
            "url": video["url"],
            "web": video["webpage_url"],
            "sure": video.get("duration", 0)
        }