from django.http import JsonResponse, HttpResponse, QueryDict
from Auth.models import User
import json
import uuid

def get_uuid():
    return uuid.uuid4()

# 检查管理员
def check(userName):
    return len(User.objects.filter(user_name=userName)) == 0

# 管理员登录
def login(request):
    request.encoding = 'utf-8'
    response = {}
    print(request.POST)
    user_name = request.POST['userName']
    password = request.POST['password']
    if check(user_name):
        response['success'] = 0
    else:
        user = User.objects.get(user_name=user_name)
        print(user.password)
        if password == user.password:
            response['success'] = 1
        else:
            response['success'] = 0
    response['code'] = 200
    return JsonResponse(response)


# 保存管理员
def save(request):
    request.encoding = 'utf-8'
    response = {}
    if check(request.POST['userName']):
        user = User(id=get_uuid(), user_name=request.POST['userName'], password=request.POST['password'])
        user.save()
        response['success'] = 1
    else:
        response['success'] = 0
    print(check(request.POST['userName']))
    response['code'] = 200
    return JsonResponse(response)

# 更新管理员
def update(request):
    request.encoding = 'utf-8'
    response_text = 'success'
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    put = QueryDict(request.body)
    # print(put.items())
    print(put.get('id'))
    # for key,val in put.items():
    #     print(val)
    # user = User.objects.get(id=1)
    # user.name = 'Google'
    # user.save()
    
    # 另外一种方式
    #Test.objects.filter(id=1).update(name='Google')
    
    # 修改所有的列
    # Test.objects.all().update(name='Google')
    return HttpResponse(response_text)

# 删除管理员
def delete(request):
    request.encoding = 'utf-8'
    print(request.body)
    return HttpResponse('success')

# 查询管理员
def list(request):
    request.encoding = 'utf-8'
    list = []
    users = User.objects.all()
    for u in users:
        user = { 'userName': u.user_name, 'password': u.password }
        print(user)
        list.append(user)
    return JsonResponse(list, safe=False)
    

# demo
# def search(request):  
#     # 初始化
#     list = []
#     request.encoding='utf-8'
#     if 'id' in request.GET and request.GET['id']:
#         message = '你搜索的内容为: ' + request.GET['id']
#         queryset = Test.objects.filter(id=request.GET['id'])
#     else:
#         message = '你提交了空表单'
#         queryset = Test.objects.all()
#     for var in queryset:
#         print(var.name, var.id)
#         res = {'name': var.name, 'id': str(var.id)}
#         list.append(res)
#     print(list)
#     print(get_uuid())
#     data = {}
#     data['data'] = list
#     return JsonResponse(data)