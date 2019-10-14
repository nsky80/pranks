from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User		# for community tab purpose
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.http import HttpResponse
from .forms import FeedbackForm
from .models import QuesSubject, SubSeries, Paper, Prank
import random

def horse(request, quessubject_id, subseries_id, horse_slug):
	# generating random images it may replaced with original content
	source = get_object_or_404(Prank, pk=random.randint(1, 13))
	messages.success(request, "College wali sheet laga liye ki nahi?")

	return render(request, template_name="main/content.html", context={"source": source})

# It contains all category of subjects
def homepage(request):
	return render(request=request, 
				  template_name="main/home.html",
				  context={"subject_list": QuesSubject.objects.all()},
				 )			 
				

# It contains topics of all subject, subject wise
def series(request, quessubject_id):
	quessubject = get_object_or_404(QuesSubject, pk=quessubject_id)
	ques_subject = get_list_or_404(SubSeries, pk=quessubject_id)
	# messages.warning(request, quessubject_id.category_title)
	return render(request, template_name='main/series.html', context={'series': ques_subject, 'quessubject': quessubject})

# List ll papers of topic 
def papers(request, quessubject_id, subseries_id):
	sub_papers = get_list_or_404(Paper, pk=subseries_id)
	return render(request, template_name="main/papers.html", context={'sub_papers': sub_papers, 'topic': get_object_or_404(SubSeries, pk=subseries_id)})

# wrong web address if encounterd
def single_slug(request, single_slug):
	# First we search any url in category and then series after that main content
	messages.success(request, "You can give feedback!")
	return render(request = request,
					template_name='main/under_construction.html',
					context = {
								})	


# This is first  page which prompt as website opened
def index(request):
    return render(request=request, 
                template_name="main/index.html",
                )			 
				
# this page is used for user feedback
def feedback(request):
	if request.method == "POST":
		form = FeedbackForm(request.POST, request.FILES)
		if form.is_valid():
			form.save(commit=True)
			messages.success(request, f"Feedback sent successfully!")
			return redirect("/home")
		else:
			messages.error(request, f"Please Write Content!")
			return render(request=request,
							template_name="main/feedback.html",
							context={"form": form})
	form = FeedbackForm
	return render(request=request, 
				template_name="main/feedback.html",
				context={"form":form}
				)


# to show all online users, not devloped completely
def community(request):
	if request.user.is_authenticated:
		active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
		user_id_list = []
		for session in active_sessions:
			data = session.get_decoded()
			user_id_list.append(data.get('_auth_user_id', None))
		# Query all logged in users based on id list
		users =  User.objects.filter(id__in=user_id_list)
		return render(request=request, 
					template_name="main/community.html",
					context={"users": users},
					)
	else:
		messages.warning(request, f"For Community Login first!")
		return redirect("main:login")

# about page
def about(request):
	messages.success(request, "Hello, World!")
	return render(request=request, 
				  template_name="main/about.html",
				  context={}
				 )

# this view used for registering new user
def register(request):
	if request.user.is_authenticated:
		return redirect("main:account")
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New account created: {username}")
			login(request, user)
			return redirect("/")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}:{form.error_messages[msg]}")

			return render(request=request,
							template_name="main/register.html",
							context={"form": form})
	form = UserCreationForm
	return render(request=request, 
				  template_name="main/register.html",
				  context={"form":form}
				 )
				 
# this view used for logout of auth. user
def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("main:index")
	
	
def login_request(request):
	if request.user.is_authenticated:
		# return HttpResponse('<script>history.back();</script>')
		return redirect("main:account")
	if request.method == "POST":
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return HttpResponse('<script>javascript:history.go(-2);</script>')
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, 
				  template_name="main/login.html",
				  context={"form":form}
				 )