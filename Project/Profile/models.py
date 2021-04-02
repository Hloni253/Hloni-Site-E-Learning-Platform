from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from Notes.models import Notes
from DefinitionsAndExplanations.models import Definition, Explanation, Videos


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    copied_notes = models.ManyToManyField(Notes, blank=True, related_name="Notes")
    saved_definitions = models.ManyToManyField(Definition,blank=True,related_name="Definitions")
    saved_explanations = models.ManyToManyField(Explanation,blank=True,related_name="Explanations")
    saved_videos = models.ManyToManyField(Videos,blank=True,related_name="Videos")
    
    
    def __str__(self):
        return str(self.user.username)

    def view_profile(self):
        return reverse('Profile:View',kwargs={"slug":self.slug})

def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance, slug=instance)
        except:
            pass
        
post_save.connect(create_profile, sender=User)
