from django.shortcuts import render
from . models import Post
from django.contrib.auth.decorators import login_required

posts=[
    {'likes':2},
    {'likes':3},
    {'likes':4},
    {'likes':5},
    {'likes':6}

]
# Create your views here.
def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'AlcherWeb/',context)
def login(request):
    return render(request, 'AlcherWeb/login.html')
def profile(request):
    return render(request, 'AlcherWeb/profile.html')
@login_required
def newpost(request):
    return render(request, 'AlcherWeb/newpost.html')
@login_required
def myposts(request):
    context={
        'posts1':posts
    }
    return render(request, 'AlcherWeb/myposts.html',context)
    