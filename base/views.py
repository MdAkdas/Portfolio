from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'base/index.html')


def posts(request):

    posts = [
        {
            'headline':'Lab Managment System',
            'sub_headline':'From idea to product. Putting my company on the map.'
        },
        {
            'headline': 'Ecommerce Website',
            'sub_headline': 'Online store with paypal payments intergration and guest user shopping'
        },
        {
            'headline': 'Static Portfolio to Django Website',
            'sub_headline': 'Building out a back-end for my personal website to make things dynamic.'
        },
    ]
    context = {'posts':posts}
    return render(request, 'base/posts.html', context)


def post(request):
    return render(request, 'base/post.html')


def profile(request):
    return render(request, 'base/profile.html')