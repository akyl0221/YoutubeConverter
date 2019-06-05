from django.core.mail import send_mail

from celery import task
import youtube_dl


@task
def convert(video_url, email):
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'media/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(video_url)
    name = result['title']
    sending_mail(email, name)


@task
def sending_mail(email, name):
    link = ('http://127.0.0.1:8000/media/' + name).replace(" ", "%20") + '.mp3'
    send_mail(
        'Download link',
        link,
        'Kel.199821@gmail.com',
        [email],
        fail_silently=False
    )
