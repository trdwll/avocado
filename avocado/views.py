import os

from django.conf import settings
from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.views.generic import View, ListView

from . models import Post


""" 
Main system methods
"""
class BlogHome(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 5
    queryset = Post.objects.all().order_by('-id').filter(publish=True)


class ViewPost(View):
    template_name = 'post.html'

    def get(self, request, year, month, slug):
        post = get_object_or_404(Post, created__year=year, created__month=month, slug=slug, publish=True)

        if post.header_image:
            return render(request, self.template_name, {'post': post, 
                'header_image': settings.MEDIA_URL+os.path.basename(post.header_image.url)})
    
        return render(request, self.template_name, {'post': post})


class CategoryList(ListView):
    model = Post
    template_name = 'categories.html'
    context_object_name = 'posts'
    paginate_by = 20
    
    def get_queryset(self):
        return get_list_or_404(Post.objects.order_by('-id'), 
            category__icontains=self.kwargs['category'], publish=True)


"""
Error pages
"""
def handler400(request):
    return render_to_response('error_pages/400.html', {}, request, status=400)

def handler403(request):
    return render_to_response('error_pages/403.html', {}, request, status=403)

def handler404(request):
    return render_to_response('error_pages/404.html', {}, request, status=404)

def handler500(request):
    return render_to_response('error_pages/500.html', {}, request, status=500)