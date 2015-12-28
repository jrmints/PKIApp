from django.conf.urls import url

from . import views

app_name="Enrollment"

urlpatterns = [
	url(r'^validate/$', views.ValidateUser.as_view(), name='validate-user'),
]
