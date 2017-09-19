from django.conf import settings

def global_settings(request):
    return {
        'BLOG_TITLE': settings.BLOG_TITLE,
        'BLOG_DESC': settings.BLOG_DESC,
        'COPYRIGHT': settings.COPYRIGHT,
    }