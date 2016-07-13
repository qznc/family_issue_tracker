from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.forms import ModelForm, HiddenInput

from .models import Issue, Comment

class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ('title', 'description', 'for_anon', 'subscriber_only')

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
        form = IssueForm(request.POST)
        if form.is_valid():
            i = form.save()
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
    i = form.save()
    return redirect('show_issue', i.issue.pk)

@require_POST
def close_issue(request):
    issue = get_object_or_404(Issue, pk=request.POST['issue_id'])
    issue.close()
    return redirect('index')
