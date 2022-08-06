from django.db import models
# #from django.utils import timezone
from django.contrib.auth.models import User

# # Create your models here.
# class Post(models.Model):
#     #date_posted=models.DateTimeField(default=timezone.now)
    
#     author=models.ForeignKey(User,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.author
     
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'
        