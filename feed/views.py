from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views import generic

from .models import Post

# from fontawesome.fields import IconField

# class PostList(generic.ListView):
#     # status 1 = published
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'

def home(request):
        return render(request, 'index.html')

# Example class based view
# class HomeView(View):
    # def get(self, request):
    #     response = HttpResponse()
    #     return response
        