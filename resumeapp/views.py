from django.shortcuts import render
from .models import Experience,Skill,Interest,Award,Education

# Create your views here.
def index(request):

    experience_list=Experience.objects.order_by('-id')
    education_list=Education.objects.order_by('-id')
    skill_list=Skill.objects.order_by('-id')
    interest_list=Interest.objects.order_by('-id')
    award_list=Award.objects.order_by('-id')

    context={

        'experience':experience_list,
        'education':education_list,
        'skill':skill_list,
        'interest':interest_list,
        'award':award_list,
    }
    return render(request,'index.html',context)