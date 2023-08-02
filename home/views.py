from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from .models import Hero,Abouts,socialplatform,Client,contact,Skill,Testimonial,services,sdescription,Project,Summary, ProfessionalExperience, Education,Message

# Create your views here.
def display_page(request):
    my_hero = Hero.objects.first()
    abouts = Abouts.objects.first()
    clients = Client.objects.first()
    social_platform = socialplatform.objects.last()
    summaries = Summary.objects.all()
    experiences = ProfessionalExperience.objects.all()
    educations = Education.objects.all()
    contacts =contact.objects.all()
    skills = Skill.objects.all()
    testimonials = Testimonial.objects.all()
    service_list = services.objects.all()
    sdescription_list = sdescription.objects.all()
    projects = Project.objects.all()
     # it gets the first object/item in the Hero table and this will return none if hero object doesnt exits
    if not my_hero:
        my_hero =  Hero.objects.create(title="Pravash") # if not exist we create a new object

    context ={
        
        'myhero':my_hero,
        'abouts': abouts,
        'social_platform':social_platform,
        'clients':clients,
        'contacts':contacts,
        'projects': projects,
        'summaries': summaries,
        'experiences': experiences,
        'educations': educations,
        'skills': skills,
        'testimonials': testimonials,
        'services': service_list,
        'sdescriptions': sdescription_list,
        'mydata': [
            "football",
            "volleyball",
            "basketball"
        ]
    }
    return render(request,'index.html',context)


def handle_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        
        mero_message = Message.objects.create(name=name,email=email,message=message,subject=subject)
        body = "Message sent by  {}\n {}".format(mero_message.name,mero_message.message)
        mero_email = EmailMessage(subject=mero_message.subject,body=body,from_email='pravashpokhrel91@gmail.com',to=['soulboundviews@gmail.com'])
        mero_email.send()
        return redirect('home:index')