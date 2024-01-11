from django.db import models
from PIL import Image
# Create your models here.
from django.core.exceptions import ValidationError
import re

def validate_phone_number(value):
    pattern = r'^\+998[0-9]{9}$'
    if not re.match(pattern, value.replace(" ", "")):
        raise ValidationError("To'g'ri telefon raqam kiriting masalan: +9981234567")
    
    
def validate_video_format(value):
    if not value.name.endswith(('.mp4', '.mov', '.avi')):
        raise ValidationError('Unsupported file format for video.')


class Advantage(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=400)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    img = models.ImageField(upload_to="tepaga_go/portfolio/")
    
    location = models.CharField(max_length=400)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Open the image using Pillow
        img = Image.open(self.img.path)

        # Resize the image
        if img.height > 800 or img.width > 800:
            output_size = (800, 800)
            img.thumbnail(output_size)
            img.save(self.img.path)

class Video(models.Model):
    
    name = models.CharField(max_length=100)
    
    video = models.FileField(upload_to="tepaga_go/portfolio/videos/", validators=[validate_video_format])

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    img = models.ImageField(upload_to="tepaga_go/blog/")
    
    
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Open the image using Pillow
        img = Image.open(self.img.path)

        # Resize the image
        if img.height > 800 or img.width > 800:
            output_size = (800, 800)
            img.thumbnail(output_size)
            img.save(self.img.path)


class OrderPlace(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, validators=[validate_phone_number])
    content = models.TextField(max_length=400)
    def __str__(self):
        return self.name
    
class Trips(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    img = models.ImageField(upload_to="tepaga_go/Trips")
    location = models.CharField(max_length=400)
    content = models.TextField()
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Open the image using Pillow
        img = Image.open(self.img.path)

        # Resize the image
        if img.height > 800 or img.width > 800:
            output_size = (800, 800)
            img.thumbnail(output_size)
            img.save(self.img.path)
