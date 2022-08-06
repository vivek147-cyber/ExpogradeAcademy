from django.contrib import admin
from .models import bookfreeclass,contactform,feedbackform,popularCourse,featuredCourse,gallery,teacher
# Register your models here.

class bfcpost(admin.ModelAdmin):
    list_display=('name','email','contactNumber','whatsappNumber')

class contactpost(admin.ModelAdmin):
    list_display=('name','email','contactNumber','whatsappNumber','query')

class feedbackpost(admin.ModelAdmin):
    list_display=('name','classes','contactNumber','feedback')

class popcourse(admin.ModelAdmin):
    list_display=('name','image','oldprice','newprice')

class featcourse(admin.ModelAdmin):
    list_display=('name','image','oldprice','newprice')


class teach(admin.ModelAdmin):
    list_display=('name','image','subject')

admin.site.register(bookfreeclass,bfcpost)
admin.site.register(contactform,contactpost)
admin.site.register(feedbackform,feedbackpost)
admin.site.register(popularCourse,popcourse)
admin.site.register(featuredCourse,featcourse)
admin.site.register(gallery)
admin.site.register(teacher,teach)

