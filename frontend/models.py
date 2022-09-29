from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class UserProfile(models.Model):
    name = models.CharField( verbose_name='Name', max_length=100)
    surname = models.CharField(max_length=100, verbose_name='Surname')

    def __str__(self):
        return self.name


class Post(models.Model):
    date = models.DateTimeField(default=timezone.now) 
    c_surname = models.CharField(max_length=100, verbose_name='Surname')
    c_name = models.CharField(max_length=100, verbose_name='Name')
    position_level = models.CharField(max_length=100, verbose_name='Position Level')
    position = models.CharField(max_length=100, verbose_name='Going For')
    party = models.CharField(max_length=100, verbose_name='Party')
    c_state = models.CharField(max_length=100, verbose_name='State', null=True, blank=True)
    c_lga = models.CharField(max_length=100, verbose_name='Local Government', null=True, blank=True)
    image = models.ImageField(verbose_name='Post Image',upload_to='uploads/')
    mani_file = models.FileField(verbose_name='Post Image', upload_to='uploads/')
    description = models.TextField(max_length=500, verbose_name='More Information about the Candidate')
    email = models.EmailField(max_length=100)
    number = models.PositiveIntegerField()
    approved = models.BooleanField(default=False)

    class Meta:
        db_table = 'dbuser'