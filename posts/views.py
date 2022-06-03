from django.shortcuts import render
# from .models import Post

# Create your views here.
def index(request):
    # posts = Post.objects.all()
    return render(request, 'index.html')

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