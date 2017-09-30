from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    sub_heading = models.CharField(max_length=128, blank=True)
    header_image = models.ImageField(blank=True)
    category = models.SlugField(max_length=32, default='Untitled') 
    body = models.TextField()
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=128)

    def __str__(self):
        return self.title + ' by ' + self.author 

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug,
            'year': '%04d' % self.created.year,
            'month': '%02d' % self.created.month
        }

        return reverse('view_post', kwargs=kwargs)


    def get_category_url(self):
        kwargs = {
            'category': self.category
        }

        return reverse('category', kwargs=kwargs)


    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
