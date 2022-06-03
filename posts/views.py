from django.shortcuts import render
from .models import Event

# Create your views here.
def index(request):
    # evs = Event.objects.all()
    return render(request, 'index.html')

def events(request, pk):
    evs = Event.objects.get(id=pk)
    return render(request, 'events.html', {'events': evs})
# def about(request):
#     return render(request, 'about.html')

# def events(request):
#     return render(request, 'events.html')
    
# def staff(request):
#     return render(request, 'staff.html')

# def socials(request):
#     return render(request, 'socials.html')

# def post(request, pk):
#     posts = Post.objects.get(id=pk)
#     return render(request, 'posts.html', {'posts': posts})