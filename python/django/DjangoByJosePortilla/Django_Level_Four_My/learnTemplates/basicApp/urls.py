from django.conf.urls import url
from basicApp import views
# could be from . import views, but basicApp seems more clear

# TEMPLATE TAGGING
app_name = 'basicApp'

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
    url(r'^index/$',views.index,name='index'),
]
