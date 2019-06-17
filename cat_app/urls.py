from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'cat_app'

urlpatterns = [
	url(r"^login/$", 
			auth_views.LoginView.as_view(
				template_name="cat_app/login.html",
			),
			name='login'),
    url(r"^logout/$", auth_views.LogoutView.as_view(), name="logout"),
    url(r'^register/$', views.Register.as_view(), name='register'),
	url(r'^(?P<pk>\d+)/$', views.UserProfileDetailView.as_view(), name='profile_detail'),
	url(r'^create_profile/$', views.UserProfileCreateView.as_view(), name='create_profile'),
	url(r'^(?P<pk>\d+)/update_profile/$', views.UserProfileUpdateView.as_view(), name='update_profile'),
]