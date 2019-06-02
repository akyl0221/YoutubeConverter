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
        result = ydl.extract_info(video_url, download=False)
    name = result['tetle']
    vid_url = result['url']
    sending_mail(email, vid_url)
    return vid_url, name


@task
def sending_mail(email, name):
    send_mail(
        'Download link',
        'You can download file from this link: {}'.format(name),
        'foto.nurbek@gmail.com',
        [email],
        fail_silently=False
    )
