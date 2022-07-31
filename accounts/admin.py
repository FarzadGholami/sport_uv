from django.contrib import admin
from .models import CustomUser
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'age', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

