from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse


def title(request, title):
    return(HttpResponse(f"Hello, {title}"))
