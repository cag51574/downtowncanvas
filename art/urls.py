from django.conf.urls import url
from . import views

app_name = 'art'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^artist_signup/$', views.artist_signup, name='artist_signup'),
#    url(r'^create_profile/$', views.create_profile, name='create_profile'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^artists/$', views.artists, name='artists'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^(?P<art_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create_art/$', views.create_art, name='create_art'),
    url(r'^(?P<art_id>[0-9]+)/delete_art/$', views.delete_art, name='delete_art'),
    url(r'^search/$', views.search, name='search'),

]

