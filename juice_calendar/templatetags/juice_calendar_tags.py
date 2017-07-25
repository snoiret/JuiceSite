from django import template
import datetime
from calendar import HTMLCalendar
from datetime import date
from django.http import HttpResponse
from django.utils.html import format_html
register = template.Library()


class ScheduleCalendar3(HTMLCalendar):#inherit the HTMLCalendar class 

	def __init__(self, meetings, firstweekday=0):
		self.firstweekday = firstweekday # 0 = Monday, 6 = Sunday
		self.meetings = meetings

	def day_cell(self, cssclass, body):
		return '<td class="%s">%s</td>' % (cssclass, body)


	def formatday(self, day, weekday):#override format day to add the occurences (meetings)
		"""
		Return a day as a table cell.
		"""
		if day == 0:
			return '<td class="noday">&nbsp;</td>' # day outside month
		else:
			cssclass = self.cssclasses[weekday]	
			cssclass += ' filled'
			body = ['<ul id ="dayCell"> ']
			date = [o.start_time.day for o in self.meetings]
			if day in date:#if there is at least 1 meeting that day	
				today_meetings = [meeting for meeting in self.meetings if meeting.start_time.date() == datetime.date(self.year, self.month,day)]
				for meeting in today_meetings:#for all the meeting that day
					body.append('<li>')
					body.append('<a href="%s/%s">' %( meeting.occurence_name.replace(' ',''), meeting.id))
					body.append(str(meeting.start_time.time())[:5])
					body.append(' ' + meeting.occurence_name)
					body.append('</a></li>')				
				body.append('</ul>')				
				return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
			
			body.append('_')
			body.append('</ul>')
			return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))

	def formatmonth(self, year, month):
		self.year, self.month = year, month
		return super(ScheduleCalendar3, self).formatmonth(year, month, 'TRUE')



@register.simple_tag
def calendar_tag_v3(meetings):
	today=date.today()
	cal = ScheduleCalendar3(meetings)
	html = cal.formatmonth(today.year, today.month)
	return format_html(html)











