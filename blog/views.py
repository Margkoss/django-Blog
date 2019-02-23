from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author':'Markos',
        'title':'Blog Post No1',
        'content':'First Blog post in foreva',
        'date':'Feb 22, 2019'
    }
    ,
    {
        'author':'Markos',
        'title':'Blog Post No2',
        'content':'Second Blog post in foreva',
        'date':'Feb 23, 2019'
    }
]


def home(request):
    context = {'posts':posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})