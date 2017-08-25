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
from .forms import FilterUserForm, FilterProductForm
from django.template.response import TemplateResponse
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

def about(request):

	return render(request,"juice_calendar/about.html") 

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

def filter_calendar(request, filt_id):
	if request.method =='POST':
		if request.META['HTTP_REFERER']=='http://127.0.0.1:8000/calendar/filter/attendees/': #let us differenciate between the different filters
			form = FilterUserForm(request.POST)
			filt_id = 'attendees'
		if request.META['HTTP_REFERER']=='http://127.0.0.1:8000/calendar/filter/product/':
			form = FilterProductForm(request.POST)
			filt_id = 'product'
	
		if form.is_valid(): #if the form has been filled out correctly
			check = form.cleaned_data.get('check')
		
			redirect_url='/calendar/results/' + filt_id + '/'
			for i in check :
				redirect_url = redirect_url +  i+'-'
			return TemplateResponse(request, 'juice_calendar/redirect_template.html',{'redirect_url':redirect_url})			

			#return HttpResponse('<script type="text/javascript">window.close(); window.parent.location.href = "/calendar/results";</script>')
			#Get the upper Product Item for the ProductTree
			#Item=ProductItem.objects.get(product_item_name='Juice') 
			
			#check occurences for all the selected users in the comnig month
			#today=date.today()
			#current_month = today.month
			#month_meetings=[]
			#meetings=[]
			#for u in check:
				#user = Profile.objects.get(id=u)
			   #	meetings=user.occurence_set.all())
			#		for meeting in meeting:
		 #	for meeting in meetings:
		#		if meeting.start_time.month == current_month: 
		#			month_meetings.append(meeting)

			return render(request,"juice_calendar/monthcalendar3.html",{'username':'Results','meetings':month_meetings, 'Item':Item}) 
	else:
		if filt_id == 'product':
			form = FilterProductForm()
		if filt_id == 'attendees':
			form = FilterUserForm()
	
	return render(request, 'juice_calendar/popup.html', {'form':form ,'filt_id': filt_id})



def filter_results(request, filt_id, list_filt):
	#Get the upper Product Item for the ProductTree
	Item=ProductItem.objects.get(product_item_name='Juice') 
	
	#Get the id list from url. 
	check=[]
	num=""
	for cha in list_filt:
		if cha !='-':
			num=num+cha
		else:
			check.append(int(num))
			num=""

#check occurences for all the selected users in the comnig month
	today=date.today()
	current_month = today.month
	month_meetings=[]
	meetings=[]
	if filt_id == 'attendees':
		for u in check:
			user = Profile.objects.get(id=u)
			meetings=user.occurence_set.all()
			for meeting in meetings:
				if meeting.start_time.month == current_month: 
					month_meetings.append(meeting)

		return render(request,"juice_calendar/monthcalendar3.html",{'username':'Results','meetings':month_meetings, 'Item':Item})












