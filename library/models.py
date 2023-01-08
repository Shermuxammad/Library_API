from django.db import models

# Create your models here.

class Kitob(models.Model):
    nomi = models.CharField(max_length=200)
    kitob_haqida = models.TextField()
    muallif = models.CharField(max_length=200)
    janr = models.CharField(max_length=100)
    
    #kitob id raqami
    isbn = models.IntegerField()
    narx = models.IntegerField()
    
    def __str__(self):
        return self.nomi