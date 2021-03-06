from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request,title):
    return render(request,'encyclopedia/wiki.html',{'wiki':util.get_entry(title),"tilte":title})

