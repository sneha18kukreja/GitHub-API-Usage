# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
import requests
from .forms import SubmitUser
from .serializers import SearchSerializer

# Create your views here.

def save_user(request):
	if request.method == "POST":
		form = SubmitUser(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			r = requests.get('https://api.github.com/users/'+name)
			rjson = r.json()
			serializer = SearchSerializer(data = rjson)
			return render(request, 'user-search.html',{'saveuser':rjson})

	else:
		form = SubmitUser()

	return render(request,'index-search.html',{'form':form})