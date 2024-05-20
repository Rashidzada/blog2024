from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name
    
class BolgPost(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=233,unique=True)
    body = models.TextField()
    image = models.ImageField(blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    video = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} By {self.author.name}"

