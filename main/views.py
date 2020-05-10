from django.shortcuts import render, redirect
from .forms import UrlForm
from .models import ShortURL
from .shortener import Shortener
# Create your views here.


def home(request, token):
    long_url = ShortURL.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)


def make(request):
    form = UrlForm(request.POST)
    a = ""
    whole_short_u = request.META['HTTP_HOST'] + '%s' % a
    if request.method == "POST":
        if form.is_valid():
            NewUrl = form.save(commit=False)
            a = Shortener().issue_token()
            NewUrl.short_url = a
            NewUrl.save()
        else:
            form = UrlForm()
            a = "Invalid URL"
    return render(request, 'home.html', {'form': form, 'a': a, 'whole_short': whole_short_u})

