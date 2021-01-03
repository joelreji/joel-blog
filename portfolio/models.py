from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    prodUrl = models.CharField(max_length=100, default="www.google.com")


    def __str__(self):
        return self.title
