from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
        

    return render(request, 'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request ,'users/profile.html')

@login_required
def mypost(request):
    return render(request ,'AlcherWeb/myposts.html')

@login_required
def newpost(request):
    return render(request ,'users/newpost.html')