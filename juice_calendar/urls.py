from django.conf.urls import url
from . import views

#app_name = 'juice_calendar'

urlpatterns = [
	url(r'^$',views.log_user, name='login'),
	url(r'^About/$',views.about, name='about'),
	url(r'^results/(?P<filt_id>[a-zA-Z0-9]*)/(?P<list_filt>([0-9]*-)*)/$', views.filter_results, name='results'),
	url(r'^filter/(?P<filt_id>[a-zA-Z0-9]*)/$',views.filter_calendar, name='filter'),
	url(r'^(?P<username>[a-zA-Z0-9]*)/$',views.calendar_user_view, name='calendar_user'),
	url(r'^(?P<username>[a-zA-Z0-9]*)/(?P<occurence>[a-zA-Z0-9]*)/(?P<occurence_id>[0-9]*)/$', views.occurence_detail, name='detail'),
#	url(r'^(?P<username>[a-zA-Z0-9]*)/(?P<product>[a-zA-Z0-9]*)/$',views.calendar_system_view, name='calendar_system'),
]
