
from django.urls import path
from . import views

app_name = 'blog'     # set the app_name , here app name is blog, it helps Django to pick the details from this app and not to get confuse with same file present in other apps


urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    
    ]
