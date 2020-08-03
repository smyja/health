from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from aview.core.models import Profile

# Create your views here.
@login_required(login_url='/login/')
def dashboard(request):
    
    w = User.objects.filter(groups__name='Hospitals')
    return render(request, 'dashboard/dasboard.html',{'w':w})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'dashboard/profile.html', context)

