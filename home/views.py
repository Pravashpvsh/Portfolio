from django.shortcuts import render
from .models import Hero,Abouts,socialplatform,Client,contact,Skill,Testimonial

# Create your views here.
def display_page(request):
    my_hero = Hero.objects.first()
    abouts = Abouts.objects.first()
    clients = Client.objects.first()
    social_platform = socialplatform.objects.last()
    contacts =contact.objects.all()
    skills = Skill.objects.all()
    testimonials = Testimonial.objects.all()
     # it gets the first object/item in the Hero table and this will return none if hero object doesnt exits
    if not my_hero:
        my_hero =  Hero.objects.create(title="Pravash") # if not exist we create a new object
 

    context ={
        
        'title':my_hero.title,
        'abouts': abouts,
        'social_platform':social_platform,
        'clients':clients,
        'contacts':contacts,
        'skills': skills,
        'testimonials': testimonials,
        'mydata': [
            "football",
            "volleyball",
            "basketball"
        ]
    }
    return render(request,'index.html',context)