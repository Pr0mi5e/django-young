from django.http import JsonResponse, HttpResponse, QueryDict
from Yongdao.models import Student
import json
import uuid

def get_uuid():
    return uuid.uuid4()

# 检查学员名称是否重复
def check_by_name(studentName):
    return len(Student.objects.filter(student_name=studentName)) == 0

# 检查学员是否存在
def check_by_id(id):
    return len(Student.objects.filter(id=id)) == 1

def list(requst):
  requst.encoding = 'utf-8'
  list = []
  students = Student.objects.all()
  for stu in students:
    student = { 'studentName': stu.student_name, 'password': stu.password, 'id': stu.id }
    list.append(student)
    print(stu.student_name)
  return JsonResponse(list, safe=False)

# 保存
def save(request):
    request.encoding = 'utf-8'
    response = {}
    if check_by_name(request.POST['studentName']):
        user = Student(id=get_uuid(), student_name=request.POST['studentName'], password=request.POST['password'])
        user.save()
        response['success'] = 1
    else:
        response['success'] = 0
    print(check_by_name(request.POST['studentName']))
    response['code'] = 200
    return JsonResponse(response)

# 更新
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

# 删除
def delete(request):
    request.encoding = 'utf-8'
    response = {}
    studentId = request.POST['studentId']
    if check_by_id(studentId):
        Student.objects.filter(id=studentId).delete()
        response['success'] = 1
    else:
        response['success'] = 0
    response['code'] = 200
    return JsonResponse(response)