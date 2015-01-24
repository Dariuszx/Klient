import requests, json, paths

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
