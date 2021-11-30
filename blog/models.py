
from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    matn = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.pk)])

class Rasm(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    rasm = models.FileField(upload_to='rasmlar/')