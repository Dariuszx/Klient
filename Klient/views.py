from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import json

import tools


def login(request):
    if request.method == "POST":
        data = json.dumps(request.POST.dict())

        tools.valid_loggin(data)
    else:
        print "nie"

    template = get_template("login.html")
    return HttpResponse(template.render(Context()))

