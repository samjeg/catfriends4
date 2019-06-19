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
    url(r"^logout/$", auth_views.LogoutView.as_view(
    		template_name="cat_app/index.html"
    	), name="logout"),
    url(r'^register/$', views.Register.as_view(), name='register'),
	url(r'^profile/(?P<pk>\d+)/$', views.UserProfileDetailView.as_view(), name='profile_detail'),
	url(r'^create_profile/$', views.UserProfileCreateView.as_view(), name='create_profile'),
	url(r'^profile/(?P<pk>\d+)/update_profile/$', views.UserProfileUpdateView.as_view(), name='update_profile'),
	url(r'^profile/(?P<pk>\d+)/delete_profile/$', views.UserProfileDeleteView.as_view(), name='delete_profile'),
	url(r'^cat_list/$', views.CatListView.as_view(), name='cat_list'),
	url(r'^create_cat/$', views.CatCreateView.as_view(), name='create_cat'),
	url(r'^cat_topic/(?P<pk>\d+)/$', views.CatDetailView.as_view(), name='cat_detail'),
	url(r'^cat_topic/(?P<pk>\d+)/update_cat/$', views.CatUpdateView.as_view(), name='update_cat'),
	url(r'^cat_topic/(?P<pk>\d+)/delete_cat/$', views.CatDeleteView.as_view(), name='delete_cat'),
]