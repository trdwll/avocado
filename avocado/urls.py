"""avocado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from . import views

handler400 = 'avocado.views.handler400'
handler403 = 'avocado.views.handler403'
handler404 = 'avocado.views.handler404'
handler500 = 'avocado.views.handler500'

urlpatterns = [
    path('', views.BlogHome.as_view(), name='home'),
    path('page/<int:page>/', views.BlogHome.as_view(), name='home_paginated'),
    path('<int:year>/<int:month>/<slug>.html', views.ViewPost.as_view(), name='view_post'),
    path('category/<category>/', views.CategoryList.as_view(), name='category'),
    path('category/<category>/page/<int:page>/', views.CategoryList.as_view(), name='category_paginated'),
    path('admin/', admin.site.urls, name='admin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
