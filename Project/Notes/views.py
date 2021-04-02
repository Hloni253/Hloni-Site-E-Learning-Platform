from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Notes, Comment
from .forms import NotesForm, CommentForm
from Profile.models import Profile
from Home.models import Topic, Grade
from django.contrib.auth.decorators import login_required
from django.db.models import Q


@login_required
def save_note(request, id):
    note = Notes.objects.get(id=id)
    profile = Profile.objects.get(user=request.user)

    profile.copied_notes.add(note)

    return redirect("/notes/view/{}".format(note.id))

@login_required
def remove_note(request, id):
    note = Notes.objects.get(id=id)
    profile = Profile.objects.get(user=request.user)

    profile.copied_notes.remove(note)

    return redirect("Profile:Profile")

def List_Notes(request):
    search_notes = None
    if request.GET:
        query = request.GET.get("search")
        search_notes = Notes.objects.filter(name__icontains=query)

    notes = Notes.objects.filter(status='Pu').order_by("-date")

    context = {
        "notes":notes,
        "search_notes":search_notes
        }

    return render(request, "Notes/ListNotes.html",context)

def Note_View(request, id):
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment.objects.create(comment=request.POST['comment'])
            comment.note = Notes.objects.get(id=id)
            comment.save()
            return redirect("/notes/view/{}".format(id))
    else:
        comments = Comment.objects.filter(note = Notes.objects.get(id=id))
        note = Notes.objects.get(id=id)

        topics = Topic.objects.all()

        if note.status == 'Pr':
            if request.user != note.user:
                return redirect('Notes:List')

        try:
            Notes.objects.get(id=str(int(id)-1))
            prev_note = Notes.objects.get(id=str(int(id)-1))
        except:
            prev_note = None

        try:
            Notes.objects.get(id=str((int(id)+1)))
            next_note = Notes.objects.get(id=str((int(id)+1)))
        except:
            next_note = None

    context = {
        "comments":comments,
        "note":note,
        "prev":prev_note,
        "next":next_note,
        }

    return render(request, "Notes/ViewNote.html", context)

@login_required
def Create_Note(request):
    topics = Topic.objects.filter(grade = Grade.objects.get(id=1))
    
    if request.method == "POST":
        print(request.POST)
        form = NotesForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            request.user.Note.add(item)
            return redirect('Profile:Profile')

    else:
        form = NotesForm()

    context = {
        "form":form,
        "topics":topics,
        }

    return render(request, "Notes/CreateNote.html", context)

@login_required
def Copy_Note(request, id):
    note = Notes.objects.get(id=id)
    if note.status == "Pr":
        return redirect("Profile:Profile")
    request.user.profile.copied_notes.add(note)
    return redirect("Profile:Profile")
