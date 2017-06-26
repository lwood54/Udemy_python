from django.conf.urls import url
from first_app_my import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]
