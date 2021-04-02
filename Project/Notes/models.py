from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from Home.models import Topic

class Notes(models.Model):
    types = (
        ('Pu','Public'),
        ('Pr','Private'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Note", null=True)
    name = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=types)
    notes = models.TextField()
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    def view_note(self):
        return reverse('Notes:View',kwargs={"id":self.id})


    @property
    def comments(self):
        return self.comment_set.all()

    def date_month(self):
        months = {1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
        return months[self.date.month]

    def first_fifty_words(self):
        return self.notes[:50]

    def save_note(self):
        return reverse("Notes:Save", kwargs={"id":self.id})

    def remove_note(self):
        return reverse("Notes:Remove", kwargs={"id":self.id})

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now=True)
    note = models.ForeignKey(Notes, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "Comment No. {}".format(self.id)
