from django import forms

class CreateNewList(forms.Form): # form name and inherit from forms.Form
	name = forms.CharField(label="Name", max_length=200)
	check = forms.BooleanField(required=False)



class DateInput(forms.DateInput):
	input_type = 'date'

class ExampleForm(forms.Form):
	my_date_field = forms.DateField(widget=DateInput)