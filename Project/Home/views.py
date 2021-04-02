from django.shortcuts import render, redirect
from .models import Subject, Grade, Topic, Concept
from django.db.models import Q
from DefinitionsAndExplanations.models import Definition, Explanation, Videos


def home(request):
    subjects = Subject.objects.all()

    grades = Grade.objects.all()

    topics = Topic.objects.all()

    context = {
        "subjects":subjects,
        "topics":topics,
        "grades":grades,
        }
    
    return render(request, "Home/home.html", context)

def concepts(request, subject_slug, grade_slug, topic_slug):
    definitions = None
    explanations = None
    videos = None
    if request.GET:
        query = request.GET.get('search')
        definitions = Definition.objects.filter(Q(term__icontains=query))
        explanations = Explanation.objects.filter(Q(title__icontains=query))
        videos = Videos.objects.filter(Q(title__icontains=query))
    subject_q = Subject.objects.filter(slug=subject_slug)
    if subject_q.exists():
        subject = subject_q.first()
    else:
        return redirect("Home:Home")
        
    grade_q = subject.grades.filter(slug=grade_slug)
    if grade_q.exists():
        grade = grade_q.first()
    else:
        grade = None
        
    topic_q = grade.topics.filter(slug=topic_slug)
    if topic_q.exists():
        topic = topic_q.first()
    else:
        topic = None
        
    concepts = Concept.objects.filter(topic=topic)

    topics = Topic.objects.all()
        
    context = {
        'grade':grade,
        'topic':topic,
        'concepts':concepts,
        'topics':topics,
        'definitions':definitions,
        'explanations':explanations,
        'videos':videos,
    }
    
    return render(request, 'Home/concepts.html', context)
    


def courses(request):

    subjects = Subject.objects.all()

    context = {
        "subjects":subjects,
        }
    
    return render(request, "Home/courses.html", context)


def blog(request):
    return render(request, "Home/blog.html")


def blog_detail(request):
    return render(request, "Home/blog_details.html")
