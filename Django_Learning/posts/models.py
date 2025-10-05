from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField(max_length=250,unique=True)

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True,blank=True, related_name='books')

