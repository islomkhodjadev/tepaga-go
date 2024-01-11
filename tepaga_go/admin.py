from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Advantage)
admin.site.register(models.Trips)
admin.site.register(models.Portfolio)
admin.site.register(models.Blog)
admin.site.register(models.Video)
admin.site.register(models.OrderPlace)