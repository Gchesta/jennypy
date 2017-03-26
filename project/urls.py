from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.presentation_list, name='presentation_list'),
]