from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Nationality


@admin.display(description='Full Name')
def full_name(obj):
    return ("%s %s" % (obj.first_name, obj.last_name))


# Register your models here.
class UserAdminConfig(UserAdmin):
    readonly_fields = ('username', )
    ordering = ('-date_joined', )
    list_display = (
        'id',
        'email',
        full_name,
        'is_active'
    )
    list_filter = ('is_active', 'is_staff', 'is_superuser', )
    fieldsets = (
        (None, {
            # 'classes': ('collapse',),
            'fields': ('email', 'password')
        }),
        ('Personal Info', {
            'classes': ('collapse',),
            'fields': (('first_name', 'last_name'),
                       'date_of_birth', 'gender', 'permanentAddress', 'presentAddress',
                       'mobilePhone', 'mobilePhone2', 'nid', 'birthCertNumber',
                       'nationality', 'fatherName', 'motherName', 'photo'
                       )
        }),
        ('Fundamental Permissions', {
            'classes': ('collapse',),
            'fields': ('is_active', 'is_staff', 'is_superuser', )
        }),
        ('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions', )
        }),
        # ('Academics', {
        #     'classes': ('collapse', ),
        #     'fields': (('isTransfered', 'joinedSemester', 'depertment', 'uid'), )
        # }),
        ('Important Dates', {
            'classes': ('collapse', ),
            'fields': (('date_joined',), )
        }),
        # ('User Settings', {
        #     'classes': ('wide',),
        #     'fields': ('is_public', 'preffered_time_zone',
        #                'default_workplace', ),
        # }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'date_of_birth', 'gender', 'permanentAddress', 'presentAddress',
                       'mobilePhone', 'mobilePhone2', 'nid', 'birthCertNumber',
                       'nationality', 'fatherName', 'motherName', 'photo', 'password1', 'password2'
                       ),
        }),
    )


admin.site.register(User, UserAdminConfig)
admin.site.register(Nationality)
