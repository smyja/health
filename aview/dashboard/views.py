from django.dispatch import receiver, Signal
from django.db.models.signals import post_save
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from aview.core.models import Profile, Appointment,Note
from aview.core.forms import EditProfileForm, PatientNotesForm
from aview.core.signals import *
# Create your views here.
@login_required(login_url='/login/')
def dashboard(request):
    
    w = User.objects.filter(groups__name='Hospitals')
    # rel_r = Appointment.objects.filter(patient=profile)
    # rel_s = Appointment.objects.filter(hospital=profile)
    
    return render(request, 'dashboard/dasboard.html',{'w':w})


def profile(request, slug, pk):
    profil = Profile.objects.get(slug=slug)
    profile = Profile.objects.get(pk=pk)
    context = {'profile': profile, 'profil': profil}
    return render(request, 'dashboard/profile.html', context)





def bookapp(request, operation, pk):
     hospital = Profile.objects.get(pk=pk)
     
     if operation == 'add':
        Appointment.create_appointment(hospital,request.user.profile)
        
        return HttpResponse('You have booked an appointment')

         

def acceptapp(request):
    if request.method == 'POST':
        id = request.POST['id']
        appointment = Appointment.objects.get(id=id)
      
        appointment.status = 'approved'
        
        appointment.save()
        

    # patient = Profile.appointment.patient.save()objects.get(pk=pk)
    # if operation == 'update':
    #     Appointment.accept_appointment(patient, status)

    return redirect('hospital')


def bookin(request):
    if request.method == 'POST':
        user_id = request.POST['id']
        hospital = Profile.objects.get(user_id=user_id)
        addapp = Appointment(hospital=hospital, patient=request.user.profile)
        addapp.save()
        context = {'hospital': hospital}
        return render(request, 'core/booked.html', context)


def edit_profile(request,slug,id):
    profile = Profile.objects.get(user_id=id)
    user = get_object_or_404(Profile, pk=id, user=profile.user.id)
    if request.method == 'POST':
       
        form = EditProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect(f'/dashboard/profile/{profile.slug}/{profile.user.pk}')
        else:
            print(form.errors)
            return HttpResponse('Could not save')

    else:
       
        form = EditProfileForm(instance=profile)
        args = {'form': form,'id':id,'slug':slug}
        return render(request, 'core/editprofile.html', args)


def addnotes(request, slug,id):
    profile = Profile.objects.get(user_id=id)
    if request.method == 'POST':
        form = PatientNotesForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['illness'],form.cleaned_data['patient'])
            form.save()
            return redirect(f'/dashboard')
    else:
        form = PatientNotesForm(initial={'patient': profile,'patientfullname':profile.get_fullname})
        
    return render(request, 'core/addnotes.html', {'form': form})

# book = Signal(providing_args=['booking'])

# def addfriend(request):
#     book.send(sender=Appointment, booking='booked')

#     return render(request, 'dashboard/addfriend.html')


# @receiver(post_save, patient=Appointment)
# def post_save_add_to_appointment_with(patient, created, instance, **kwargs):
#     patient_ = instance.patient
#     hospital_ = instance.hospital
#     if instance.status == 'approved':
#         patient_.appointment_with.add(patient_.User)
#         hospital_.appointment_with.add(hospital_.User)
#         patient_.save()
#         hospital_.save()
#     print(kwargs)


# class ProfileListView(ListView):
#     model = Profile
#     template_name = 'dashboard/profile.html'

#     def get_queryset(self):

