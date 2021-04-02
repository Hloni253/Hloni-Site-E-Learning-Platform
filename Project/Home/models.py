from django.db import models
from django.urls import reverse


class Subject(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    
    def __str__(self):
        return self.title

    @property
    def grades(self):
        return self.grade_set.all()

class Grade(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=None)
    image_url = models.CharField(max_length=100,default=None,blank=True)
    
    def __str__(self):
        return self.title

    @property
    def topics(self):
        return self.topic_set.all()


class Topic(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    @property
    def concepts(self):
        return self.concept_set.all()

    @property
    def videos(self):
        return self.videos_set.all()

    def my_url(self):
        return reverse('Home:Concepts', kwargs={'subject_slug':self.grade.subject.slug, 'grade_slug':self.grade.slug, 'topic_slug':self.slug})

class Concept(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.title

    @property
    def explanations(self):
        return self.explanation_set.all()

    @property
    def definitions(self):
        return self.definition_set.all()

