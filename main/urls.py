from django.urls import path
from django.conf.urls import url
from . import views


app_name = "main"

urlpatterns = [
	
	path('', views.index, name="home"),
	url(r'^filter', views.filter, name="filter"),
	url(r'^bespoke-filter', views.bespoke_filter, name="bespoke-filter"),

	]