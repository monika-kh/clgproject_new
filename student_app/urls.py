from django.urls import path, include
from student_app import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("college/", views.CollegeView.as_view()),
    path("college/<int:pk>/", views.CollegeView.as_view(), name="college"),
    path("student/", views.StudentView.as_view()),
    path("student/<int:pk>/", views.StudentView.as_view(), name="student"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path("send-mail/", views.SendEmailView.as_view()),
    path("index", views.IndexView.as_view(), name='index'),
    path("college_by_name/", views.PrintCollegeNameView.as_view()),
    #path('rest-auth/', include('rest_auth.urls')),
]







