from django.shortcuts import render, redirect
from .models import Definition, Explanation, Videos
from Profile.models import Profile
from django.contrib.auth.decorators import login_required


@login_required
def save_definition(request, id):
    definition = Definition.objects.get(id=id)
    profile = Profile.objects.get(user=request.user)

    profile.saved_definitions.add(definition)
    concept = definition.concept

    return redirect("/concept/{}/{}/{}".format(concept.topic.grade.subject.slug,concept.topic.grade.slug,concept.topic))

@login_required
def remove_definition(request, id):
    definition = Definition.objects.get(id=id)
    profile = Profile.objects.get(user=request.user)

    profile.saved_definitions.remove(definition)

    return redirect("Profile:Profile")

@login_required
def save_explanation(request, id):
    explanation = Explanation.objects.get(id=id)
    profile = Profile.objects.get(user=request.user)

    profile.saved_explanations.add(explanation)
    concept = explanation.concept

    return redirect("/concept/{}/{}/{}".format(concept.topic.grade.subject.slug,concept.topic.grade.slug,concept.topic))

@login_required
def remove_explanation(request, id):
    explanation = Explanation.objects.get(id=id)
    profile = Profile.objects.get(user=request.user)

    profile.saved_explanations.remove(explanation)

    return redirect("Profile:Profile")

@login_required
def save_video(request, id):
    video = Videos.objects.get(id=id)
    profile = Profile.objects.get(user=request.user)

    profile.saved_videos.add(video)
    topic = video.topic

    return redirect("/concept/{}/{}/{}".format(topic.grade.subject.slug,topic.grade.slug,topic.slug))

@login_required
def remove_video(request, id):
    video = Videos.objects.get(id=id)
    profile = Profile.objects.get(user=request.user)

    profile.saved_videos.remove(video)

    return redirect("Profile:Profile")








