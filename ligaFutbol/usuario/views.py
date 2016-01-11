from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from forms import SignUpForm

# Create your views here.

def signup(request):
	if request.method == 'POST':  # If the form has been submitted...
		form = SignUpForm(request.POST)  # A form bound to the POST data
		if form.is_valid():  # All validation rules pass

			user=form.save()
			user.set_password(user.password)

			user.save()

			return HttpResponseRedirect('/')  # Redirect after POST
	else:
		form = SignUpForm()

	context={'form':form}
	return render(request,'signup.html',context)
