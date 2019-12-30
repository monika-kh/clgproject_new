from django.contrib.auth import authenticate
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework import status, authentication, permissions
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import College, Student
from .serializers import (
    CollegeSerializer,
    RelatedCollegeSerializer,
    Student1Serializer,
    StudentSerializer,
    # StudentRegisterSerializer
    #LoginInSerializer)
)
from .services import (
    CollegeService,
    CreateStudentService,
    DeleteCollegeService,
    GetCollegeService,
    GetRelatedStudentService,
    GetStudentService,
    PutCollegeService,
    # GetRegisterService,
    # CreateRegisterService,
    DeleteRelatedStudentService,
    # GetEmailService,
    send_varification_email,
    IndexService,
    PrintCollegeByNameService)


# Create your views here.
from .tasks import send_mail_to_all, print_no, print_clgname


#
# def index(request):
#     send_mail_to_all.delay(request)
#     return HttpResponse('done')

class CollegeView(APIView):
    #permission_classes = (IsAuthenticated,)

    def post(self, request):
        college_data = request.data
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            college = CollegeService.execute({"college_data": request.data})
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request, pk=None):  # pk is used to get clg id
        college_gt = GetCollegeService.execute({"pk": pk})
        if pk:
            serializer = CollegeSerializer(college_gt)
        else:
            serializer = CollegeSerializer(college_gt, many=True)
        return Response(serializer.data)

    # clg_get = GetCollegeService.execute({})
    # serializer = CollegeSerializer(clg_get, many=True)
    # return Response(serializer.data)

    def delete(self, request, pk):
        DeleteCollegeService.execute({"pk": pk})
        return Response(data={"Message": "deleted"}, status=200)

    def put(self, request, pk):
        college_put = College.objects.get(pk=pk)
        data = request.data
        serializer = CollegeSerializer(college_put, data=request.data)
        if serializer.is_valid():
            # PutCollegeService.execute({'pk': pk})
            PutCollegeService.execute(
                {'college_put': college_put, 'data': request.data}
            )  # data sent to services
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







class StudentView(APIView):
    # permission_classes = (IsAuthenticated,)


    def post(self, request):
        student_data = request.data
        serializer = Student1Serializer(data=student_data)  # when obj is not created
        if serializer.is_valid(raise_exception=True):
            college = CreateStudentService.execute({"student_data": request.data})
            ser1 = Student1Serializer(college)         # when obj is created
            return Response(ser1.data, status=201)
        return Response(serializer.errors, status=400)


    def get(self, request, pk=None):  # get students related to a particular college id
        related_student = GetRelatedStudentService.execute({"pk": pk})
        college_gt = GetCollegeService.execute({"pk": pk})
        if pk:
            serializer = RelatedCollegeSerializer(college_gt)
        else:
            serializer = RelatedCollegeSerializer(college_gt, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        DeleteRelatedStudentService.execute({'pk': pk})
        return Response(data={"Message": "deleted"}, status=200)


class SendEmailView(APIView):
     def post(self, request, pk=None):

         email_msg=request.data.get("message")
         email_sub=request.data.get("subject")
         # students_in = Student.objects.all()
         #
         # for student in students_in:
         #     email = student.email
         #     send_varification_email(email_sub, email_msg, email)
         send_mail_to_all.delay(email_msg, email_sub)
         return Response(data={"Message": "success"}, status=200)


class IndexView(APIView):
    def post(self, request):
        # print no between 1 10 2000 using celery using service , views and task
        IndexService.execute({})
        return Response(data={"Message":"printed"}, status=200)



        # print no between 1 10 2000 using celery using views and task
        # for i in (a,b):
        #     print(i)
        # print_no.delay(1,2001)
        # return Response(data={"Message":"printed"}, status=200)



class PrintCollegeNameView(APIView):
    def post(self, request):
        college_data = request.data
        serializer = CollegeSerializer(data=college_data)
        if serializer.is_valid(raise_exception=True):
            college = PrintCollegeByNameService.execute({"college_data":serializer.data})
            # return Response(serializer.data, status=201)

        return Response(data={"Message":"printed"}, status=200)


















































































































































# class RegisterView(APIView):
#     def get(self, request):
#         student_register = Student.objects.all()
#         student_get = GetRegisterService.execute({'student_register': student_register})           # get all data
#         serializer = StudentSerializer(student_get, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         register_data = request.data
#         serializer = StudentSerializer(data=request.data)  # when obj is not created
#         if serializer.is_valid(raise_exception=True):
#             student = CreateRegisterService.execute({"register_data": request.data})
#             ser1 = StudentSerializer(student)  # when obj is created
#             return Response(ser1.data, status=201)
#         return Response(serializer.errors, status=400)
#


