from django.conf.urls import patterns,url

from online_forms import views;

urlpatterns = patterns('',
			url(r'^login/$',views.login, name = 'login'),
			url(r'^signup/$',views.signup, name = 'signup'),
			url(r'^fill/(?P<form_hash>\w+)/$',views.fill_form,name='fill'),
			url(r'^view/(?P<form_hash>\w+)/$',views.view_form,name='view'))
