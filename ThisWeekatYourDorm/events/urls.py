from django.conf.urls import url
from . import views

app_name = 'events'
urlpatterns = [
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'), # here
    url(r'^calendar/(?P<week>\d)/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^calendar/(?P<week>\d)/(?P<cat>\w+)/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^calendar/(?P<week>\d)/(?P<cat>\w+)/(?P<eve>[\w|\W]+)/$', views.CalendarView.as_view(), name='calendar')
]
