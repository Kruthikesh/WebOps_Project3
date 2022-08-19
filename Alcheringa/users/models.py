from django.db import models
# #from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from AlcherWeb.models import Post
# # Create your models here.
# class Post(models.Model):
#     #date_posted=models.DateTimeField(default=timezone.now)
    
#     author=models.ForeignKey(User,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.author
     
class Profile(models.Model):
    
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='Profile')
    image = models.ImageField(default='profile_pics/default.jpg',upload_to='profile_pics')
    


    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        img=Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)        



