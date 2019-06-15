from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.BlogHome.as_view(), name='home'),
    path('page/<int:page>/', views.BlogHome.as_view(), name='home_paginated'),
    path('<int:year>/<int:month>/<slug>.html', views.ViewPost.as_view(), name='view_post'),
    path('category/<category>/', views.CategoryList.as_view(), name='category'),
    path('category/<category>/page/<int:page>/', views.CategoryList.as_view(), name='category_paginated'),
    path('admin/', admin.site.urls, name='admin'),

    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
