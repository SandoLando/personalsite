from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'personalsite'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('resume', views.ResumeView, name='resume'),

    ]
