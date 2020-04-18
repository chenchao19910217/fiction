from django.shortcuts import render

# Create your views here.
import hashlib

from django.http import HttpResponse
from django.shortcuts import render
import json
# Create your views here.
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie



# Create your views here.
from . import models

def hash_code(s, salt='mysite'):# 加点盐
    h = hashlib.sha256()
    s += salt
    print(s)
    h.update(s.encode())
    # update方法只接收bytes类型
    print(h)
    return h.hexdigest()

@csrf_exempt
@ensure_csrf_cookie
def index(request):
    return HttpResponse("首页")

