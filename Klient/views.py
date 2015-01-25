# encoding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
import json, settings, paths, requests

import tools

def user_accout_template(username):
    template = get_template("user_account.html")
    context = Context()
    context.push({"username" : username})
    return context, template

def login(request):
    if tools.is_logged(request):
        return HttpResponseRedirect("/")

    context = Context()

    if request.method == "POST":
        data = json.dumps(request.POST.dict())

        response = tools.valid_loggin(data)

        if response != 0:
            #TODO tworzę sesje użytkownika
            resp = json.loads(response)
            tools.login_user(request, resp['user_id'], json.loads(data)['login'])
            return HttpResponseRedirect("/")
        else:
            context.push({"message":"Niepoprawne dane logowania"})


    #Template logowania jeżeli niezalogowany
    template = get_template("login.html")
    return HttpResponse(template.render(context))

def index(request):
    if not tools.is_logged(request):
        return HttpResponseRedirect("/login")

    template = get_template("user_account.html")
    context = Context()

    context.push({"username" : request.session['login']})


    return HttpResponse(template.render(context))

def logout(request):
    tools.logout_user(request)
    return HttpResponseRedirect('/login')

def my_ideas(request):
    if not tools.is_logged(request):
        return HttpResponseRedirect("/login")

    context, template = user_accout_template(request.session['login'])
    context.push({"option" : "ideas"})

    headers = {"Content-Type": "text/plain"}
    path = paths.get_user_idea + str(request.session['user_id'])
    result = requests.get(path)

    if result.status_code == 200:
        data = json.loads(result.text)
        context.push({"ideas" : data})

    return HttpResponse(template.render(context))

def show_idea(request, idea_id):
    if not tools.is_logged(request):
        return HttpResponseRedirect("/login")

    context, template = user_accout_template(request.session['login'])
    context.push({"option" : "threads"})

    headers = {"Content-Type": "text/plain"}
    path = paths.get_idea_threads + str(idea_id)
    result = requests.get(path)

    if result.status_code == 200:
        data = json.loads(result.text)
        context.push({'threads' : data})

    return HttpResponse(template.render(context))

def show_thread(request, thread_id):
    if not tools.is_logged(request):
        return HttpResponseRedirect("/login")

    context, template = user_accout_template(request.session['login'])
    context.push({"option" : "notes"})
    context.push({"thread_id" : thread_id})

    headers = {"Content-Type": "text/plain"}
    path = paths.get_thread_notes + str(thread_id)
    result = requests.get(path)

    if result.status_code == 200:
        data = json.loads(result.text)
        context.push({"notes" : data})

    return HttpResponse(template.render(context))

def new_note(request, thread_id):
    if not tools.is_logged(request):
        return HttpResponseRedirect("/login")

    if request.method == "POST" and request.POST.dict().has_key('content'):
        dic = request.POST.dict()
        dic['user_id'] = request.session['user_id']
        dic['thread_id'] = thread_id

        data = {"user_id":request.session['user_id'], "thread_id":thread_id, "content":dic['content']}

        path = paths.new_note

        r = requests.post(path, data=data)

        print r.text

        if r.status_code == 200:
            return HttpResponseRedirect("/show/thread/"+str(thread_id))


    context, template = user_accout_template(request.session['login'])
    context.push({"option" : "new_note"})

    return HttpResponse(template.render(context))


