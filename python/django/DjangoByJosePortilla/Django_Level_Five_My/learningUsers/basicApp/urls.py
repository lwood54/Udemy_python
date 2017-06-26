from django.conf.urls import url
from basicApp import views
from django.conf import settings
from django.conf.urls.static import static

# TEMPLATE URLS!
app_name = 'basicApp'

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^special/$',views.special,name='special'),
]
