from django.contrib import admin

from viodes import models

admin.site.register(models.User)
admin.site.register(models.CategoryVid)
admin.site.register(models.CategoryImg)
admin.site.register(models.Img)
admin.site.register(models.Videos)
admin.site.register(models.AutoVideoFile)
