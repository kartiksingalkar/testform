from django.shortcuts import render
from .models import interviewform

# Create your views here.

def index(request):
    if request.method == 'POST':
        print('working')
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        print(first_name,last_name,'data printed')
        data = interviewform(first_name=first_name,last_name=last_name)
        data.save()
    return render (request,'base.html')