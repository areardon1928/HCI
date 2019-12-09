from django.conf.urls import url
from . import views

app_name = 'events'
urlpatterns = [
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'), # here
    url(r'^calendar/(?P<cat>\w+)/$', views.CalendarView.as_view(), name='calendar')
]
