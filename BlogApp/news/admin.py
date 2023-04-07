from django.contrib import admin
from .models import Articles
from .models import CustomUser

admin.site.register(Articles)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser',)


