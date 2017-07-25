import datetime
import calendar
from datetime import date
from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from .models import Occurence, ProductItem, Profile, Event

# Create your views here.

def log_user(request):
	username = request.user.username
	if request.user.is_authenticated():
		login(request, request.user)
        # Redirect to a success page.
		return HttpResponseRedirect(reverse('calendar_user', kwargs={'username':username})) 
	else:
        #Try again.
		return HttpResponseRedirect(reverse('login')) 

def log_out(request):
	logout(request)
	return render(request,"registration/login.html") 

def calendar_view(request):
	return render(request,"juice_calendar/monthcalendar.html", {'username':'John'}) 

def calendar_other_view(request,username):
	return render(request,"juice_calendar/monthcalendar2.html",{'username':username}) 

def calendar_user_view (request,username):
	user_id=request.user.pk
	user=get_object_or_404(User, pk=user_id)
	#Get the upper Product Item for the ProductTree
	Item=ProductItem.objects.get(product_item_name='Juice') 

	#Check the occurences in the upcoming month
	today=date.today()
	current_month = today.month
	meetings = user.profile.occurence_set.all()
	month_meetings=[]
	for meeting in meetings:
		if meeting.start_time.month == current_month: 
			month_meetings.append(meeting)

	return render(request,"juice_calendar/monthcalendar3.html",{'username':username,'meetings':month_meetings, 'Item':Item}) 

def occurence_detail(request,username,occurence,occurence_id):
	# See the detail of an occurence 

	Item=ProductItem.objects.get(product_item_name='Juice') 
	meeting=Occurence.objects.get(pk=occurence_id)
	attendees=meeting.attendee.all()
	return render(request, "juice_calendar/occurence_detail.html", {'meeting':meeting,'attendees':attendees, 'Item':Item})

def calendar_system_view (request,product,username):
	#Get the upper Product Item for the ProductTree
	Item=ProductItem.objects.get(product_item_name='Juice') 
	currentItem=ProductItem.objects.get(product_item_name=product) 
	
	#Check the occurences in the upcoming month
	today=date.today()
	current_month = today.month
	events = currentItem.event_set.all()#queryset
	month_meetings=[]

	for ev in events:
		ev_month_meetings = ev.occurence_set.filter(start_time__month=current_month)	#queryset
		for meeting in ev_month_meetings:
			month_meetings.append(meeting) #list

	return render(request,"juice_calendar/monthcalendar_product.html",{'currentItem': currentItem,'username':username, 'meetings':month_meetings, 'Item':Item}) 

def modify_event(request, username):
	#Needed: check authorization
	#try:
		#user is authorized
	#except "user not authorized":
		#raise "You don't have authorization to do that

	return render(request, 'juice_calendar/modify_event.html')

def create_event(request, username):
		#Needed: check authorization
	#try:
		#user is authorized
	#except "user not authorized":
		#raise "You don't have authorization to do that
 
	return render(request, 'juice_calendar/create_event.html')























