from django import forms
from .models import Occurence, ProductItem, Profile, Event
class FilterUserForm(forms.Form):
	all_users=Profile.objects.all()
	CHOICES = []
	for user in all_users:
		full_name = user.user.first_name +' '+ user.user.last_name
		CHOICES.append((user.id, full_name))

	check = forms.MultipleChoiceField(choices=CHOICES, widget = forms.CheckboxSelectMultiple())

class FilterProductForm(forms.Form):
	all_products=ProductItem.objects.all()
	CHOICES = []
	for product in all_products:
		CHOICES.append((product.id, product.product_item_name))

	check = forms.MultipleChoiceField(choices=CHOICES, widget = forms.CheckboxSelectMultiple())

