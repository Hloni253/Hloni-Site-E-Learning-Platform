from django.db import models
from Home.models import Concept, Topic
from django.urls import reverse

class Definition(models.Model):
    term = models.CharField(max_length=100)
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.term

    @property
    def definitionsforterm(self):
        return self.definitionsforterm_set.all()

    def save_definition(self):
        return reverse("Definition:Save_Def", kwargs={"id":self.id})

    def remove_definition(self):
        return reverse("Definition:Remove_Def",kwargs={"id":self.id})



class DefinitionsForTerm(models.Model):
    definition_for_term = models.TextField()
    definition = models.ForeignKey(Definition, on_delete=models.CASCADE)

    def __str__(self):
        return self.definition_for_term

class Explanation(models.Model):
    title = models.CharField(max_length=100,default=None)
    explanation_for_concept = models.TextField()
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def explanationlinks(self):
        return self.explanationlinks_set.all()

    def save_explanation(self):
        return reverse("Definition:Save_Exp", kwargs={"id":self.id})

    def remove_explanation(self):
        return reverse("Definition:Remove_Exp",kwargs={"id":self.id})

class ExplanationLinks(models.Model):
    title = models.CharField(max_length=100)
    links = models.CharField(max_length=100)
    explanation = models.ForeignKey(Explanation, on_delete=models.CASCADE,blank=True,default=None)

    def __str__(self):
        return self.title

class Videos(models.Model):
    title = models.CharField(max_length=100)
    links = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,blank=True,default=None)

    def __str__(self):
        return self.title

    def save_video(self):
        return reverse("Definition:Save_Vid", kwargs = {"id":self.id})

    def remove_video(self):
        return reverse("Definition:Remove_Vid", kwargs = {"id":self.id})



















