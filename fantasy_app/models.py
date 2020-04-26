from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=40)
    slug = models.SlugField(editable=False,unique=True)
    home_city = models.CharField(max_length=40)
    logo = models.ImageField(upload_to="logo/")

    def __str__(self):
        return self.team_name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.team_name)
        super().save(*args,**kwargs)

class Player(models.Model):
    player_name = models.CharField(max_length=40)
    player_image = models.ImageField(upload_to='player/')
    credit = models.PositiveIntegerField()
    points = models.PositiveIntegerField()
    designation=models.CharField(max_length = 30, choices = [('WK','WicketKeeper'),('BAT','Batsman'),('BOWL','Bowler'),('ALL','All Rounder')])
    team = models.ForeignKey(Team,related_name='players',on_delete=models.CASCADE)
    slug = models.SlugField(editable=False,unique=True)


    def __str__(self):
        return self.player_name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.player_name)
        super().save(*args,**kwargs)


class Match(models.Model):
    team1 = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE,related_name='team2')
    time = models.TimeField(auto_now=False, auto_now_add=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
    venue = models.CharField(max_length=30)

    #functions


    
