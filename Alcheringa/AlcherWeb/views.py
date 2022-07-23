from django.shortcuts import render
posts=[
    {'likes':2},
    {'likes':3},
    {'likes':4},
    {'likes':5},
    {'likes':6}

]
# Create your views here.
def login(request):
    return render(request, 'AlcherWeb/login.html')
def profile(request):
    return render(request, 'AlcherWeb/profile.html')
def newpost(request):
    return render(request, 'AlcherWeb/newpost.html')
def myposts(request):
    context={
        'posts1':posts
    }
    return render(request, 'AlcherWeb/myposts.html',context)