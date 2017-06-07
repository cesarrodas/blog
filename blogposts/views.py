from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def home(request):
    Blog_Posts = BlogPost.objects.order_by('-pub_date')
    return render(request, 'blogposts/home.html', {'BlogPosts': Blog_Posts})
