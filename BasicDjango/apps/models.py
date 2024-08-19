from datetime import datetime

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey('apps.Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Job(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Staff(models.Model):
    fullname = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='staff/')
    facebook_account = models.CharField(max_length=100)
    twitter_account = models.CharField(max_length=100)
    email_account = models.CharField(max_length=100)
    job = models.ForeignKey('apps.Job', on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname


class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Organizer(models.Model):
    name = models.CharField(max_length=100)

class Speaker(models.Model):
    fullname = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='staff/')
    room = models.ForeignKey('apps.Room', on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    organizer = models.ForeignKey('apps.Organizer', on_delete=models.CASCADE)

    @property
    def sub_time(self):
        datetime1 = datetime.combine(datetime.min, self.start_time)
        datetime2 = datetime.combine(datetime.min, self.end_time)

        # Subtract the datetime objects
        time_difference = datetime2 - datetime1

        # Print the difference
        return time_difference
    def __str__(self):
        return self.fullname

class Region(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey('apps.Region', on_delete=models.CASCADE , related_name="districts")
    def __str__(self):
        return self.name


