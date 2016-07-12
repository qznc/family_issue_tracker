from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from .models import Issue, Comment

def index(request):
    issues = Issue.objects.all();
    context = dict(issues=issues)
    return render(request, 'issue_list.html', context)

@require_POST
def create(request):
    context = dict()
    return render(request, 'edit_issue.html', context)

def show(request, id):
    issue = get_object_or_404(Issue, pk=id)
    context = dict(issue=issue)
    return render(request, 'show_issue.html', context)
