from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request, question_id):
	return HttpResponse("You're looking at question %s.")
def results(request, wuestion_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)
def vote(request, question_id):
	return HttpResponse("you're voting on question %s." % question_id)