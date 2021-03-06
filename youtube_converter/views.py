from django.shortcuts import render

from youtube_converter.forms import UrlForm
from youtube_converter.models import Download
from youtube_converter.tasks import convert


def index(request):
    urlform = UrlForm()
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            email = form.cleaned_data.get('email')
            Download.objects.create(url=url, email=email)
            convert.delay(url, email)
        return render(request, "youtube_converter/home.html", {"form": urlform})
    else:
        return render(request, "youtube_converter/home.html", {"form": urlform})


def history(request):
    downloads = Download.objects.all()
    return render(request, "youtube_converter/history.html", {"urls": downloads})