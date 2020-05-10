from django.conf.urls import url
from covid_19 import views

urlpatterns = [
	url(r'^home/$',views.greetings),
    url(r'^home/search$',views.search),
]
