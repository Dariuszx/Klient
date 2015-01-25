# encoding: utf-8
import requests, json, paths
from django.http import HttpResponseRedirect

#Sprawdzam czy podane dane logowania są poprawne względem bazy danych
#Dane wejściowe to login i password w JSONie
def valid_loggin(json_data):
    headers = {"Content-Type": "text/plain"}
    path = paths.login

    data = json.loads(json_data)

    if len(data['login']) < 5 and len(data['password']) < 5:
        return 0

    r = requests.post(path, data=data)
    if r.status_code == 200:
       return r.text
    else:
        return 0

def login_user(request, user_id, login):
    request.session['login'] = login
    request.session['user_id'] = user_id

def logout_user(request):
    if "login" in request.session and "user_id" in request.session:
        del request.session['login']
        del request.session['user_id']

def is_logged(request):
    if not "user_id" in request.session or not "login" in request.session:
        return False
    else:
        return True