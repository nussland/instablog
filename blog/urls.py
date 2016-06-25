from django.conf.urls import url

from .views import *

app_name = 'blog'

urlpatterns = [
    url(r'^posts/create/$', create_post, name='create'),
    url(r'^posts/(?P<pk>[0-9]+)/$', detail_post, name='detail'),
    url(r'^$', list_posts, name='list'),
]