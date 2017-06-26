from django.conf.urls import url
from newApp import views

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^users/$',views.users,name='users'), #### THIS MIGHT BE AN ISSUE??? with the whole no table thing
]
