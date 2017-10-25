from django import forms
from .models import SearchUsers
class SubmitUser(forms.Form):
	name = forms.CharField()
	class Meta:
		model=SearchUsers #or whatever object
