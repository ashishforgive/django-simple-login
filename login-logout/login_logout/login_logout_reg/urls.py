from django.conf.urls import url

from . import views

urlpatterns = [
	
    url(r'/', views.indexView),
    url(r'^login/', views.loginView),


]