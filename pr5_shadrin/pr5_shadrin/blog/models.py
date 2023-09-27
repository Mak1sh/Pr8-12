from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    body = models.TextField()


    def ＿str＿(self):
        return self.title



# Create your models here.
