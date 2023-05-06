from django.db import models
from django.contrib.auth.models import User

class Opinion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.IntegerField(default=5)
    opinion = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, )
    
    def __str__(self):
        return self.user.username
    