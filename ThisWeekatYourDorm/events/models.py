from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

# Create your models here.
class Event(models.Model):
        title = models.CharField(u'Event Title', max_length=200, unique=True)
        day = models.DateField(u'Day of the event', help_text=u'Day of the event')
        start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
        end_time = models.TimeField(u'Final time', help_text=u'Final time')
        notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)
        category = models.CharField(u'Event Category', max_length=50)

        class Meta:
            verbose_name = u'Scheduling'
            verbose_name_plural = u'Scheduling'
	
        def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
            overlap = False
            if new_start == fixed_end or new_end == fixed_start:    #edge case
                overlap = False
            elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
                overlap = True
            elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
               overlap = True
 
            return overlap
 
        def get_absolute_url(self, weeknum):
            url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
            color = "black"
            if (self.category=="Sports"):
                color = "darkcyan"
            elif (self.category=="Academic"):
                color = "forestgreen"
            elif (self.category=="Music"):
                color = "orangered"
            elif (self.category=="Entertainment"):
                color = "purple"
            elif (self.category=="Community"):
                color = "goldenrod"
            return u'<a href="%s" style="color: %s;">%s</a>' % (str(self.title), color, str(self.title))
 
        def clean(self):
            if self.end_time <= self.start_time:
                raise ValidationError('Ending times must after starting times')
 
            events = Event.objects.filter(day=self.day)
            if events.exists():
                for event in events:
                    if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                        raise ValidationError(
                            'There is an overlap with another event: ' + str(event.day) + ', ' + str(
                                event.start_time) + '-' + str(event.end_time))

