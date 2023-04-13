from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    YES = 'Available'
    NO = 'None'
    staf = [
        (YES, 'Available'),
        (NO, 'None')
    ]
    home_img = models.ImageField(default='default/img.png')
    about_img = models.ImageField(default='default/img.png')
    name = models.CharField(max_length=200)
    degree = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    brithday = models.DateTimeField()
    experience = models.CharField(max_length=100)
    email = models.EmailField()
    frilance = models.CharField(choices=staf, max_length=15, default=NO)
    currently = models.CharField(max_length=500, blank=True, null=True)
    skills = models.ManyToManyField('Skills')


    def __str__(self):
        return self.name

class Skills(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=50, validators=[
        MaxValueValidator(100),
        MinValueValidator(1)
    ])

    def __str__(self):
        return self.name






class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Portfolio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    link = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_activated = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Images(models.Model):
    img = models.ImageField()
    author = models.ForeignKey(Portfolio,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.img.name)

