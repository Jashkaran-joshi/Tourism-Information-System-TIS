from django.shortcuts import render
from .models import TeamMember

# Create your views here.

def about(request):
    team_members = TeamMember.objects.all()
    return render(request, 'about.html', {
        'team_members': team_members
    })