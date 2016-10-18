from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.conf import settings
from datetime import datetime
from PIL import Image

class BaseProject(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=30, blank = True, null = True)
    going_on = models.BooleanField(blank=True, default=False)
    start_date = models.DateField(blank = True, null = True)
    end_date = models.DateField(blank = True, null = True)
    github_url = models.CharField(max_length=50, null= True, blank = True)
    class Meta:
        abstract = True
            
@python_2_unicode_compatible
class RequestProject(BaseProject):
    published_date = models.DateTimeField(default=datetime.now, blank=True)
    email = models.EmailField(max_length=70, blank = True)
    def __str__(self):
        return "Requested Project: {}". format(self.title)
    
@python_2_unicode_compatible
class SelfProject(BaseProject):
    def __str__(self):
        return "Self Project: {}". format(self.title) 

@python_2_unicode_compatible
class WorkProject(BaseProject):
    professor =  models.CharField(max_length=30, null=True, blank=True)
    course =  models.CharField(max_length=50, null=True, blank=True)
    published_date = models.DateTimeField(default=datetime.now, blank=True, null = True)
    email = models.EmailField(max_length=70, blank = True, null = True)
    def __str__(self):
        return "Academic Project: {}". format(self.title)
     
    
class Images(models.Model):
    work_project = models.ForeignKey(WorkProject)
    images = models.ImageField()
    
    def save(self):
        if not self.images:
            return 
        
        super(Images, self).save()
        image = Image.open(self.images)
        (width, height) = image.size
        new_height = 500
        new_width = 500 * width/height     
        size = ( new_width, new_height)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.images.path)