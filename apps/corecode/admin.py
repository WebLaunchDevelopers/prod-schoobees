from django.contrib import admin
from .models import SiteConfig, AcademicSession, AcademicTerm, Subject, StudentClass, Calendar, Driver

class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'user')

class AcademicSessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'current', 'user')
    list_filter = ('user', 'current')

class AcademicTermAdmin(admin.ModelAdmin):
    list_display = ('name', 'current', 'user')
    list_filter = ('user', 'current')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name',)

class StudentClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name',)

class CalendarAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'type', 'user')
    search_fields = ('title',)

class DriverAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'phone_number', 'email')
    search_fields = ('user', 'name', 'phone_number', 'email', 'address', 'aadhaar_number', 'license_number', 'vehicle_number')
    list_filter = ('user', 'vehicle_name', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Driver, DriverAdmin)
admin.site.register(SiteConfig, SiteConfigAdmin)
admin.site.register(AcademicSession, AcademicSessionAdmin)
admin.site.register(AcademicTerm, AcademicTermAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(StudentClass, StudentClassAdmin)
admin.site.register(Calendar, CalendarAdmin)