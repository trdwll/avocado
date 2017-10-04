from django.conf import settings

def global_settings(request):
    return {
        'BLOG_TITLE': settings.BLOG_TITLE,
        'BLOG_DESC': settings.BLOG_DESC,
        'COPYRIGHT': settings.COPYRIGHT,

        'TWTTR_LNK': settings.TWTTR_LNK,
        'GITHUB_LNK': settings.GITHUB_LNK,
        'FB_LNK': settings.FB_LNK,
        'REDDIT_LNK': settings.REDDIT_LNK,
    }