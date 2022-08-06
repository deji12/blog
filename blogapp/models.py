from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category1(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category2(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    image = models.FileField(upload_to='blog-post-image')
    first_category = models.ForeignKey(Category1, on_delete=models.CASCADE)
    second_category = models.ForeignKey(Category2, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    number_of_clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.title

#post, name, body, date
class Comment(models.Model):
    name = models.CharField(max_length=225)
    post_name = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post_name)


