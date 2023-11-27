from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to='post/%m', blank=True)
    cost = models.PositiveIntegerField(null=True)
    created_date = models.DateField(auto_now_add=True)



