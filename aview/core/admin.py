from django.contrib import admin
from .models import Profile,Appointment,Note
# Register your models here.
admin.site.register(Profile)


class AppointmentAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Appointment, AppointmentAdmin)


class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Note,NoteAdmin)
