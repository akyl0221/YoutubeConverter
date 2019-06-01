from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import UrlForm
from .models import Download
from .downloader import converter


def index(request):
    urls = Download.objects.all()
    urlform = UrlForm()
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            video_url = converter(url)
            Download.objects.create(url=url)
            return HttpResponseRedirect(video_url)
        return render(request, "youtube_converter/home.html", {"form": urlform}, {"urls": urls})
    else:
        return render(request, "youtube_converter/home.html", {"form": urlform}, {"urls": urls})
