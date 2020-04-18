import hashlib,os

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
    md5 = hashlib.md5()
    s += salt
    md5.update(s.encode('utf-8'))
    md5.hexdigest()
    return md5.hexdigest()

@csrf_exempt
@ensure_csrf_cookie
def index(request):

    return HttpResponse("index")

@csrf_exempt
def personal(request):

    if request.session.get('user_id', 0) > 0:
        try:
            user_id = request.session.get('user_id')
            user = models.User.objects.get(userid=user_id)
            message = json.dumps({'header': {'resCode': 0, 'resMsg': 'success'}, 'body': {'name':user.name,'userid':user.userid,'headurl':user.head_img}})
        except:
            message = json.dumps({'header': {'resCode': 1, 'resMsg': 'error:没有该用户'}, 'body': {}})
            return HttpResponse(message)
    else:
        message = json.dumps({'header': {'resCode': 1, 'resMsg': 'error:没有登录'}, 'body': {}})
    return HttpResponse(message)

@csrf_exempt
def head_images(request):
    if request.session.get('user_id', 0) > 0:
        try:
            user_id = request.session.get('user_id')
            print(user_id)
            user = models.User.objects.get(userid=user_id)
            ret_file = request.FILES.get("photo")
            path = str(os.path.abspath('.'))
            with open(path + '/login/static/images/' + str(user.userid)+'.jpg', 'wb') as f:
                for i in ret_file.chunks():
                    f.write(i)
            user.head_img = 'http://127.0.0.1:8000/static/images/' + str(user.userid) + '.jpg'
            user.save()
            message = json.dumps({'header': {'resCode': 0, 'resMsg': 'success:修改头像成功'}, 'body': {}})
            return HttpResponse(message)
        except:
            message = json.dumps({'header': {'resCode': 1, 'resMsg': 'error:用户名不存在'}, 'body': {}})
            return HttpResponse(message)
    else:
        message = json.dumps({'header': {'resCode': 1, 'resMsg': 'error:没有登录'}, 'body': {}})
        return HttpResponse(message)

@csrf_exempt
def login(request):

    if request.session.get('user_id',0) > 0:
        print(request.session.get('user_id'))
        print(request.session.session_key)
        message = json.dumps({'header': {'resCode': 1, 'resMsg': 'error:重复登录'}, 'body': {}})
        return HttpResponse(message)

    if request.method == "POST":
        postBody = request.body
        json_result = json.loads(postBody)
        if json_result['body']['name'] and json_result['body']['password']:
            new_name = json_result['body']['name']
            password1 = json_result['body']['password']
            try:
                user = models.User.objects.get(name=new_name)
            except:
                message = json.dumps({'header': {'resCode': 1, 'resMsg': 'error:用户名不存在'}, 'body': {}})
                return HttpResponse(message)
            print(user.password)
            password1=hash_code(password1)
            if user.password == password1:
                request.session['user_id'] = user.userid
                message = json.dumps({'header': {'resCode': 0, 'resMsg': 'success:登录成功'}, 'body': {}})
                return HttpResponse(message)
            else:
                message = json.dumps({'header': {'resCode': 1, 'resMsg': 'error:密码错误'}, 'body': {}})
                return HttpResponse(message)
        else:
            message = json.dumps({'header': {'resCode': 1, 'resMsg': 'error:不能为空'}, 'body': {}})
            return HttpResponse(message)
    else:
        message = json.dumps({'header': {'resCode': 1, 'resMsg': 'error:请求错误'}, 'body': {}})
        return HttpResponse(message)

@csrf_exempt
@ensure_csrf_cookie
def register(request):
    message = {
               'header': {'resCode': 0, 'resMsg': 'success'},
               'body': {'token':''}
               }
    if request.method == "POST":
        postBody = request.bodype
        print('11111111',postBody)
        json_result = json.loads(postBody)
        if json_result['body']['name'] and json_result['body']['password1'] and json_result['body']['c_time'] and json_result['body']['password2']:
            new_name = json_result['body']['name']
            password1 = json_result['body']['password1']
            password2 = json_result['body']['password2']
            c_time=json_result['body']['c_time']
            if password1 != password2:
               message = json.dumps({'header': {'resCode': 1, 'resMsg': 'error:密码不一致'}, 'body': {}})
               return HttpResponse(message)
            else:
               username = models.User.objects.filter(name=new_name)
               if username:
                   message = json.dumps({'header': {'resCode': 1, 'resMsg': 'error:用户名已存在'}, 'body': {}})
                   return HttpResponse(message)
               new_user = models.User()
               new_user.name = new_name
               print(hash_code(password1))
               new_user.password = hash_code(password1)
               new_user.c_time = c_time
               new_user.save()
               message = json.dumps({'header': {'resCode': 0, 'resMsg': 'success'}, 'body': {}})
               return HttpResponse(message)
        else:
            message = json.dumps({'header': {'resCode': 1, 'resMsg': 'error:不能为空'}, 'body': {}})
            return HttpResponse(message)
    else:
        message = json.dumps({'header': {'resCode': 0, 'resMsg': 'error:请求错误'}, 'body': {}})
        return HttpResponse(message)

@csrf_exempt
def logout(request):
    if request.method == "POST":
        request.session.flush()
        # print(request.session.get('user_id'))
        message = json.dumps({'header': {'resCode': 0, 'resMsg': 'success:退出成功'}, 'body': {}})
        return HttpResponse(message)
    message = json.dumps({'header': {'resCode': 0, 'resMsg': 'error:请求错误'}, 'body': {}})
    return HttpResponse(message)
