from django.shortcuts import render
from .models import Issue,Submission

def noise_home(request):
    latest_issue=Issue.objects.latest('publication_date')
    poems=latest_issue.pieces.all()
    all_issues=Issue.objects.all()
    recent_issues=all_issues[:3]
    context={'issue':latest_issue,'poems':poems,'all_issues':all_issues,'recent_issues':recent_issues}
    return render(request, 'noise-home.html',context)

def noise_issue(request,slug):
    issue=Issue.objects.get(slug=slug)
    poems=issue.pieces.all()
    all_issues=Issue.objects.all()
    recent_issues=all_issues[:3]
    context={'issue':issue,'poems':poems,'all_issues':all_issues,'recent_issues':recent_issues}
    return render(request, 'noise-home.html',context)

def noise_submit(request):
    submissions=Submission.objects.all()
    context={'submissions':submissions}
    return render(request,'submissions-noise.html',context)
