from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from fantasy_app.models import Player
from django.utils.text import slugify

# Create your models here.

User = get_user_model()
class UserTeam(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    total_points = models.PositiveIntegerField(null=True,blank=True)
    slug = models.SlugField(editable=False,unique=True,blank=True,null=True)

    
    def __str__(self):
        return self.user.username+"'s Team"

    def save(self,*args,**kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args,**kwargs)


    def get_absolute_url(self):
        return reverse('user_team:create')


class UserPlayer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    player = models.ForeignKey(Player,on_delete = models.CASCADE,null=True)

    def __str__(self):
        return self.player.player_name

    
        
