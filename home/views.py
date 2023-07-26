from django.shortcuts import render
from .models import Hero,facts,socialplatform 
# Create your views here.
def display_page(request):
    my_hero = Hero.objects.first()
    facts_data = facts.objects.all() 
    social_platform = socialplatform.objects.last()
     # it gets the first object/item in the Hero table and this will return none if hero object doesnt exits
    if not my_hero:
        my_hero =  Hero.objects.create(title="Pravash") # if not exist we create a new object
    if not facts_data:    
        facts.objects.create(paragraph="nvidvnoidnudisuifhuewfubcuicbibisiwdscuiiubcibscd")

    context ={
        # 'title':"Welcome to BMC DHARAN",
        'title':my_hero.title,
        'facts_data': facts_data,
        'social_platform':social_platform,
    
        'mydata': [
            "football",
            "volleyball",
            "basketball"
        ]
    }
    return render(request,'index.html',context)