from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse
from AlcherWeb.models import Post
from users.models import Profile
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
    if request.method == 'POST':

        u_form=UserUpdateForm(request.POST, instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.Profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Account updated!')
            return redirect('profile')



    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.Profile)
    
    
    context={
    'u_form':u_form,
    'p_form':p_form
        }
    return render(request ,'users/profile.html',context)

@login_required
def mypost(request):
    return render(request ,'AlcherWeb/myposts.html')

@login_required
def newpost(request):
    return render(request ,'users/newpost.html')

@login_required
def favourite_add(request,id):
    post=get_object_or_404(Post,id=id)
    if post.favourites.filter(id=request.user.id).exists():
        print()
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
    # user=request.user
    # post=Post.objects.get(id=post_id)
    # profile=Profile.objects.get(user=user)

    # if profile.saved_posts.filter(id=post_id).exists():
    #     print('already saved')

    # else:
    #     profile.saved_posts.add(post)
    # return render(request,'users/saved_post.html')


    # pk = self.kwargs.get('pk')
    # 
    # spost.saved_posts.add(request.user)
    

# class PostListView(ListView):
#     model=Post


@login_required
def favourite_list(request):
    new=Post.objects.all().filter(favourites=request.user)
    return render(request,'users/saved_post.html',{'new':new})