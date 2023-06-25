from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, page):
    markdown = markdown2.markdown_path(f"entries/{page}.md")
    return render(request, f"encyclopedia/entry.html", {
        "markdown": markdown,
        "page": page
    })
