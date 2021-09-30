from django.http import JsonResponse, HttpResponse, QueryDict
from Yongdao.models import Student
import json
import uuid

def get_uuid():
    return uuid.uuid4()

# 检查管理员
def check(studentName):
    return len(Student.objects.filter(student_name=studentName)) == 0

def list(requst):
  requst.encoding = 'utf-8'
  list = []
  students = Student.objects.all()
  for stu in students:
    student = { 'studentName': stu.student_name, 'password': stu.password }
    list.append(student)
    print(stu.student_name)
  return JsonResponse(list, safe=False)

# 保存管理员
def save(request):
    request.encoding = 'utf-8'
    response = {}
    if check(request.POST['studentName']):
        user = Student(id=get_uuid(), student_name=request.POST['studentName'], password=request.POST['password'])
        user.save()
        response['success'] = 1
    else:
        response['success'] = 0
    print(check(request.POST['studentName']))
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


def delete(request):
    request.encoding = 'utf-8'
    print(request.body)
    return HttpResponse('success')