from django.db import models

class Catagory(models.Model):
    catagory = models.CharField(max_length=100)
    def __str__(self):
        return self.catagory

class Quotes(models.Model):
    q_code = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    quotes = models.CharField(max_length=1000)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
