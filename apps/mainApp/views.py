from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from . models import Users, Dogs, Requests, Pals, Messages, Playdates

def index(request):
	user =  request.session['log_user_id']
	data={
		'user':Users.objects.get(id = user),
	}
	return render(request, 'mainApp/index.html', data)