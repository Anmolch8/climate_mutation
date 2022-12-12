from django.contrib import admin

# Register your models here.
from climate_app.models import *

admin.site.register(disaster)
admin.site.register(images_of_change)
admin.site.register(video)
admin.site.register(blog)
admin.site.register(ngo)
admin.site.register(faq)
#admin.site.register(volunteer)
admin.site.register(cause)
admin.site.register(effect)
admin.site.register(action)
admin.site.register(expert)
admin.site.register(user_register)
admin.site.register(help_support)
admin.site.register(causes_category)
admin.site.register(contact)
admin.site.register(entitie)
admin.site.register(dataset)
admin.site.register(perdiction)
admin.site.register(evidence)




@admin.register(visuals)
class visualadmin(admin.ModelAdmin):
     list_display=('link','visual_name')

@admin.register(review)
class reviewadmin(admin.ModelAdmin):
    list_display=('id','user_name','heading')




