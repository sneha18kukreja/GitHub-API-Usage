from django import forms

class SubmitUser(forms.Form):
	name = forms.CharField()
