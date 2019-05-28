import youtube_dl

ydl_opts = {
    'format': 'best',
    'outtmpl': 'media/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
def converter(video_url):

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(video_url,download=False)

    vid_url = result['url']
    return vid_url