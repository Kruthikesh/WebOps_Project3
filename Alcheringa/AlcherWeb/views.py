from django.shortcuts import render
from . models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from users.models import Profile

# Create your views here.
# @login_required
# def home(request):
#     context={
#         'posts':Post.objects.all()
#     }
#     return render(request,'AlcherWeb/home.html',context)

class PostListView(LoginRequiredMixin,ListView):
    model=Post
    template_name='AlcherWeb/home.html'
    context_object_name='posts'
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['posted_pic','content']
    def form_valid(self,form):
        # print("from form", form.instance.content)
        form.instance.author=self.request.user
        return super().form_valid(form)
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(PostCreateView, self).get_form(form_class)
        form.fields['content'].widget.attrs ={'placeholder': 'Add Caption To Your Post'}
        return form

def login(request):
    return render(request, 'AlcherWeb/login.html')
def profile(request):
    return render(request, 'AlcherWeb/profile.html')
#decorators 
@login_required
def newpost(request):
    return render(request, 'AlcherWeb/newpost.html')
@login_required
def myposts(request):
    context={
         'posts':Post.objects.filter(author=request.user),
         'image':request.user.Profile.image
    }
    return render(request, 'AlcherWeb/myposts.html',context)
