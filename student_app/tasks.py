from celery import shared_task
from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from .models import Student, College


@shared_task
def send_mail_to_all(email_msg, email_sub):
    students_in = Student.objects.all()

    for student in students_in:
        email = student.email
        send_mail(
            email_sub,
            email_msg,
            EMAIL_HOST_USER,
            [email],
            html_message=email_msg,
            fail_silently=False,
        )

@shared_task
def print_no(a,b):
    # print no between 1 10 2000 using celery

    for i in range(1,2001):
        print(i)


@shared_task
def print_clgname(college):
    for college_name in range (1,11):

        create_obj = College.objects.create(college_name=college.get('college_data').get('college_name'),
                                        city=college.get('college_data').get('city'),
                                        state=college.get('college_data').get('state'))



