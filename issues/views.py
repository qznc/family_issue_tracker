from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.forms import ModelForm, HiddenInput

from urllib.parse import unquote

from .models import Issue, Comment, SandstormUser

def remember_sandstorm_user(request):
    sid = request.META.get('HTTP_X_SANDSTORM_USER_ID', None)
    if sid == "anonym":
        return None
    name = unquote(request.META.get('HTTP_X_SANDSTORM_USERNAME', "name?"))
    handle = request.META.get('HTTP_X_SANDSTORM_HANDLE', "handle?")
    gender = request.META.get('HTTP_X_SANDSTORM_PREFERRED_PRONOUNS', "gender?")
    try:
        u = SandstormUser.objects.get(sid=sid)
        u.name = name
        u.handle = handle
        u.gender = gender
    except SandstormUser.DoesNotExist:
        u = SandstormUser(sid=sid,name=name,handle=handle,gender=gender)
    u.save()
    return u

class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ('title', 'description', 'for_anon', 'subscriber_only', 'responsible')

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'issue')
        widgets = {'issue': HiddenInput()}

def index(request):
    open = Issue.objects.filter(closed=None).all();
    context = dict(issues=open)
    return render(request, 'issue_list.html', context)

def edit(request, id):
    issue = get_object_or_404(Issue, pk=id)
    if request.method == "POST":
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('show_issue', id)
    else:
        form = IssueForm(instance=issue)
    context = dict(form=form)
    return render(request, 'edit_issue.html', context)

def create(request):
    if request.method == "POST":
        u = remember_sandstorm_user(request)
        form = IssueForm(request.POST)
        if form.is_valid():
            i = form.save(commit=False)
            i.creator = u
            i.save()
            return redirect('show_issue', i.pk)
    else:
        form = IssueForm()
    context = dict(form=form)
    return render(request, 'edit_issue.html', context)

def show(request, id):
    issue = get_object_or_404(Issue, pk=id)
    cf = CommentForm()
    context = dict(issue=issue, commentform=cf)
    return render(request, 'show_issue.html', context)

@require_POST
def create_comment(request):
    form = CommentForm(request.POST)
    assert form.is_valid()
    u = remember_sandstorm_user(request)
    i = form.save(commit=False)
    i.creator = u
    i.save()
    return redirect('show_issue', i.issue.pk)

@require_POST
def close_issue(request):
    issue = get_object_or_404(Issue, pk=request.POST['issue_id'])
    issue.close()
    return redirect('index')

@require_POST
def reopen_issue(request):
    issue = get_object_or_404(Issue, pk=request.POST['issue_id'])
    issue.reopen()
    return redirect('show_issue', issue.pk)
