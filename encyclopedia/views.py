from tkinter import Widget
from django.shortcuts import render
from django.http import HttpResponseRedirect
from markdown2 import Markdown
from django.urls import reverse
import random
from . import util

markdowner = Markdown()

def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html")
    else:
        title = request.POST["title"]
        content = request.POST["content"]
        list_entries_lower = []
        for item in util.list_entries():
            list_entries_lower.append(item.lower())
        if title.lower() in list_entries_lower:
            return render(request, "encyclopedia/new_page.html", {"title": title})
        else:
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("title", kwargs={"title": title}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def edit(request):
    if request.method == "GET":
        title = request.GET["page_title"]
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title, "content": content})
    title = request.POST["page_title"]
    content = request.POST["content"]
    util.save_entry(title, content)
    return HttpResponseRedirect(reverse("title", kwargs={"title": title}))
        
def title(request, title): 
    list_titles_lower = []
    for item in util.list_entries():
        list_titles_lower.append(item.lower())
    if title.lower() in list_titles_lower:
        return render(request, "encyclopedia/title.html", {
            "title": markdowner.convert(util.get_entry(title)), "name": title})
    else:
        return render(request, "encyclopedia/title.html", {
            "non_existent_title": title})

def search(request):
    search_str = str(request.GET.get("q"))
    list_entries = util.list_entries()
    list_matches = []
    for entry in list_entries:
        if search_str.lower() == entry.lower():
            return HttpResponseRedirect(reverse(
                "title", kwargs={"title": entry}))
        elif search_str.lower() in entry.lower():
            list_matches.append(entry)
    return render(request, "encyclopedia/search.html", {
        "titles": list_matches, "search_str": search_str})

def random_page(request):
    random_entry = util.list_entries()[random.randint(0, len(util.list_entries())-1)]
    return HttpResponseRedirect(reverse("title", kwargs={"title": random_entry}))
