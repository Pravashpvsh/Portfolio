from django.contrib import admin
from .models import Hero,Abouts,Client,socialplatform,contact,Skill,Testimonial,services,skiill_description,cSkill,sdescription,Project,Summary, ProfessionalExperience, Education
# Register your models here.
admin.site.register(Hero)
admin.site.register(Abouts)
admin.site.register(socialplatform)
admin.site.register(Client)
admin.site.register(Skill)
admin.site.register(Testimonial)
admin.site.register(contact)
admin.site.register(services)
admin.site.register(skiill_description)
admin.site.register(cSkill)
admin.site.register(sdescription)
admin.site.register(Project)
admin.site.register(Summary)
admin.site.register(ProfessionalExperience)
admin.site.register(Education)