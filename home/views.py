from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.


from django.views.generic.base import View
from json import loads


# def index(response):
#  return render(response, "main/base.html.", {})


# def home(response):
# return render(response, "main/home.html", {})


# def about(response):
# return render(response, "main/about.#html", {})


# def blogs(response):
# return render(response, "main/blogs.3html", {})


class BasePageView(View):
    def get(self, request):
        return render(request, 'main/base.html')


class HomePageView(View):
    def get(self, request):
        return render(request, 'main/home.html')


class AboutPageView(View):
    def get(self, request):
        return render(request, 'main/about.html')


class BlogsPageView(View):
    def get(self, request):
        return render(request, 'main/blogs.html')
