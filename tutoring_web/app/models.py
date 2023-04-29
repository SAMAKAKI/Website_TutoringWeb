from django.db import models
from django.contrib.auth.models import User

class Opinion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.IntegerField(max_length=1, default=5)
    opinion = models.TextField()
    
