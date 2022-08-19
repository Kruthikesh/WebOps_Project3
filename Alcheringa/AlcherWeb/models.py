from django.db import models
#from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# from users.models import Profile
# Create your models here.
class Post(models.Model):
    # id = models.ForeignKey(Profile,on_delete=models.CASCADE)
    #date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    posted_pic = models.ImageField(default='default.jpg',upload_to='posted_pics')
    content = models.TextField(default='')
    favourites=models.ManyToManyField(User,related_name='favourite',default=None,blank=True)
    # profile_pic=models.ForeignKey(Profile,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}'s Post"

    def get_absolute_url(self):
        return reverse('AlcherWeb-home')
    # def __init__(self, *args, **kwargs):
    #     super().init(*args, **kwargs)    
     
