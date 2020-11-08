from django.shortcuts import render

# Create your views here.
import json
from django.db import models
from polls.models import Choice,People
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def clear(request):
    # Choice.objects.all().delete()
    for i in range(1,12):
        try:
            object=Choice.objects.get(Choice_id=i)
            object.votes=0
            object.save()
        except:
            pass
    People.objects.all().delete()
    return HttpResponse("sucess")
def results(request, question_id):
    for i in range(1, 12):
        Choice.objects.update_or_create(Choice_id=i)
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
def update(request,json_data):
    print(json_data)
    people= json.loads(json_data)
    name= people.get("name")
    votes= people.get("vote")
    Vote_json=json.dumps(votes)
    obj, created = People.objects.get_or_create(PName=name)
    obj = People.objects.get(PName=name)
    obj.PVote = Vote_json
    obj.save()
    if  not created :
        return  HttpResponse("already_vote")
    for vote in votes:
        print(vote)
        v= Choice.objects.get(Choice_id=vote)
        v.votes+=1
        v.save()

    return  HttpResponse("sucess")

def get_all_people(request):
    query_set=People.objects.all()
    all_people=[]
    for i in query_set.iterator():
        t={
            "name":i.PName,
            "vote":json.loads(i.PVote),
        }
        all_people.append(t)
    return  HttpResponse(json.dumps(all_people))

def vote(request, question_id):
    obj=Choice.objects.get(Choice_id=question_id)
    return HttpResponse(obj.votes)