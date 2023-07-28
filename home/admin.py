from django.contrib import admin
from .models import Hero,Abouts,Client,socialplatform,contact,Skill,Testimonial
# Register your models here.
admin.site.register(Hero)
admin.site.register(Abouts)
admin.site.register(socialplatform)
admin.site.register(Client)
admin.site.register(Skill)
admin.site.register(Testimonial)
admin.site.register(contact)