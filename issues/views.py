from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.forms import ModelForm

from .models import Issue, Comment

class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ('title', 'description', 'for_anon', 'subscriber_only')

def index(request):
    issues = Issue.objects.all();
    context = dict(issues=issues)
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
    context = dict(issue=issue)
    return render(request, 'show_issue.html', context)
