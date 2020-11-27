from django.contrib import admin
from .models import competitor
from .models import competition
# Register your models here.

admin.site.register(competitor)
admin.site.register(competition)