from django.shortcuts import render
import datetime
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from .models import *
from .utils import EventCalendar

# Create your views here.
class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/homepage/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        after_day = self.request.GET.get('day__gte', None)

        if not after_day:
            d = datetime.date.today()
        else:
            try:
                split_after_day = after_day.split('-')
                d = datetime.date(year=int(split_after_day[0]), month=int(split_after_day[1]), day=1)
            except:
                d = datetime.date.today()

        cal = EventCalendar()

        check = self.kwargs.get('cat', None)
        
        cat = check
        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(d.year, d.month, cat=cat, withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context


