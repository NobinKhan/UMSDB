from django.contrib import admin
from .models import User, Nationality, Designation, Profile, PreviousEducation
from django.contrib.auth.admin import UserAdmin


@admin.display(description='Full Name')
def full_name(obj):
    return ("%s %s" % (obj.first_name, obj.last_name))


# Register your models here.
@admin.register(User)
class UserAdminConfig(UserAdmin):
    readonly_fields = ('username', )
    ordering = ('-date_joined', )
    list_display = (
        'id',
        'username',
        'email',
        'designation',
        'is_active',
    )
    list_filter = ('isStudent', 'is_staff', 'is_superuser','isTeacher' )
    fieldsets = (
        ('Login Info', {
            # 'classes': ('collapse',),
            'fields': ('username','email', 'password', 'is_active', 'designation')
        }),
        ('Personal Info', {
            'classes': ('collapse',),
            'fields': (
                'date_of_birth', 'gender', 
            )
        }),
        ('Student Info', {
            'classes': ('collapse',),
            'fields': ('isStudent', 'studentAddmissionType', 'program', 'joinedSemester')
        }),
        ('Teacher Info', {
            'classes': ('collapse',),
            'fields': ('isTeacher', 'department',)
        }),
        ('Staff Info', {
            'classes': ('collapse',),
            'fields': ('is_staff',)
        }),
        ('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions', )
        }),
        ('Important Dates', {
            'classes': ('collapse', ),
            'fields': (('date_joined',), 'joinedSession')
        }),
    )
    add_fieldsets = (
        ('Login Info', {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', ),
        }),
        ('Personal Info', {
            'classes': ('collapse',),
            'fields': ('date_of_birth', 'gender')
        }),
        ('Student Info', {
            'classes': ('collapse',),
            'fields': ('isStudent', 'studentAddmissionType', 'program', 'joinedSemester')
        }),
        ('Teacher Info', {
            'classes': ('collapse',),
            'fields': ('isTeacher', 'department',)
        }),
        ('Staff Info', {
            'classes': ('collapse',),
            'fields': ('is_staff',)
        }),
        ('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions', )
        }),
        ('Important Dates', {
            'classes': ('collapse', ),
            'fields': (('date_joined',), 'joinedSession')
        }),
    )



@admin.register(Nationality)
class NationalityAdmin(admin.ModelAdmin):
    list_display = ('id','name',)


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ('id','name',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user','first_name', 'last_name')



@admin.register(PreviousEducation)
class PreviousEducationAdmin(admin.ModelAdmin):
    list_display = ('id','user')


