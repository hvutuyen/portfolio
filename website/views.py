from django.shortcuts import render
from website.models import Projects

# Create your views here.
def index(request):
    all_apps = Projects.objects.all()
    context = {
        'Projects': all_apps # key will be used in html
    }
    return render(request, 'website/index.html', context)