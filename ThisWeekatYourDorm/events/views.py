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
        weeknum = int(self.kwargs.get('week', 0))
        cat = check
        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(d.year, d.month, cat=cat, weeknum=weeknum, withyear=True)
        context['calendar'] = mark_safe(html_cal)
        if (check != None):
            context['filt'] = check
        context['weeknumber'] = mark_safe(weeknum)
        context['nextweek'] = mark_safe(self.get_next_week(weeknum))
        context['prevweek'] = mark_safe(self.get_prev_week(weeknum))
        return context

    def get_next_week(self, curweek):
        if (curweek < 5):
            return curweek+1
        else:
            return curweek

    def get_prev_week(self, curweek):
        if (curweek > 0):
            return curweek-1
        else:
            return curweek
