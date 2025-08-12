# from django.views import generic

# from blog.models import Post

# class PostView(generic.View):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = "index.html"

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = "post_detail.html"

###### CÓDIGO MODIFICADO ######

from django.views import View, generic
from django.shortcuts import render
from blog.models import Post

class PostView(View):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"

    def get(self, request):
        posts = self.queryset
        return render(request, self.template_name, {'posts': posts})


class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"
