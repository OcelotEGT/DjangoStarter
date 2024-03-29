"""User admin classes"""

#Django
from django.contrib import admin

#Local
from users.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_link = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number',
    )

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
    )
    
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )
