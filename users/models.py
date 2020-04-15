from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.storage import default_storage as storage
from django.conf import settings
from django.core.files import temp as tempfile
from django.core.files.base import File
from django.core.files.uploadedfile import InMemoryUploadedFile
import os
import sys

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
           im = Image.open(self.image)
           output = BytesIO()
           im = im.resize((100, 100))
           im.save(output, format='JPEG', quality=90)
           output.seek(0)  
           self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
           super(Profile,self).save()






           
            
           #super(CachedS3BotoStorage, self).save(*args, **kwargs)
            #img =Image.open(self.image.name)

            #if img.height >300 or img.width >300:
             #   output_size =(300,300)
              #  img.thumbnail(output_size)
               # img.save(self.image.name)
