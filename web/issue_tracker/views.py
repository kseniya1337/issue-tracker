from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from issue_tracker.forms import CreateIssueForm, EditIssueForm, AvatarChangeForm, CreateCommentForm
from issue_tracker.models import Issue, User, comment
from issue_tracker.models.comment import Comment


@login_required
def index(request: HttpRequest) -> HttpResponse:
    issues = Issue.objects.all()

    return render(request, 'index.html', {
        'issues_open': issues.filter(status=Issue.STATUS.open),
        'issues_in_progress': issues.filter(status=Issue.STATUS.in_progress),
        'issues_testing': issues.filter(status=Issue.STATUS.testing),
        'issues_production': issues.filter(status=Issue.STATUS.production),
    })


@login_required
def search_issue(request: HttpRequest) -> HttpResponse:
    issues = Issue.objects.all()
    query = request.GET.get('query')
    if query:
        issues = issues.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    return render(request, 'search_issues.html', {
        'issues': issues,
    })


@login_required
def profile(request: HttpRequest, username: str, ) -> HttpResponse:
    user = get_object_or_404(User, username=username)
    issues = Issue.objects.all()
    return render(request, 'profile.html', {
        'user': user,
        'issues': issues.filter(assignee=user),
        'change_avatar_form': AvatarChangeForm(),
    })


@login_required
def create_issue(request: HttpRequest) -> HttpResponse:
    form = CreateIssueForm(request.POST or None)
    if form.is_valid():
        issue = form.save(commit=False)
        issue.author = request.user
        issue.save()
        return redirect('issue_detail', issue.id)
    return render(request, 'create_issue.html', {
        'form': form,
    })


@login_required
def edit_issue(request: HttpRequest, id: str) -> HttpResponse:
    id = int(id)
    issue = get_object_or_404(Issue, id=id)
    form = EditIssueForm(request.POST or None, instance=issue)
    if form.is_valid():
        form.save()
        return redirect('issue_detail', issue.id)
    return render(request, 'edit_issue.html', {
        'form': form,
        'issue': issue,
    })


@login_required
def issue_detail(request: HttpRequest, id: str) -> HttpResponse:
    id = int(id)
    issue = get_object_or_404(Issue, id=id)
    return render(request, 'issue_detail.html', {
        'issue': issue,
        'create_comment_form': CreateCommentForm(),

    })


@login_required
@require_POST
def change_avatar(request: HttpRequest) -> HttpResponse:
    form = AvatarChangeForm(request.POST, files=request.FILES, instance=request.user)
    if form.is_valid():
        form.save()
    return redirect('profile', request.user.username)


@login_required
def create_comment(request: HttpRequest, id: str) -> HttpResponse:
    id = int(id)
    get_object_or_404(Issue, id=id)
    form = CreateCommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.issue_id = id
        comment.save()
    return redirect('issue_detail', id)


@login_required
def delete_comment(request: HttpRequest, issue_id: str, comment_id: str) -> HttpResponse:
    issue_id = int(issue_id)
    comment_id = int(comment_id)
    get_object_or_404(Issue, id=issue_id)
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    comment.delete()
    return redirect('issue_detail', issue_id)
