from django.db import models
from django.conf import settings

class BlogPost(models.Model):
    title = models.CharField(max_length = 200, unique=True)
    
    
    
    
    

