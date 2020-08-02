from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from aview.core.models import Profile

# Create your views here.
@login_required(login_url='/login/')
def dashboard(request):
    profile = (Profile.objects.filter(user=request.user))
    return render(request, 'dashboard/dasboard.html')