from django.shortcuts import render

from .forms import UrlForm
from .models import Download
from .tasks import convert


def index(request):
    urlform = UrlForm()
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            email = form.cleaned_data.get('email')
            convert.delay(url, email)
            Download.objects.create(url=url, email=email)
        else:
            return render(request, "youtube_converter/home.html", {"form": urlform})
    else:
        return render(request, "youtube_converter/home.html", {"form": urlform})
