# from django.urls import reverse
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.authtoken.models import Token
from rest_framework.test import force_authenticate
from rest_framework.permissions import IsAuthenticated

from ..models import College, Student


class College_Test(APITestCase):  # without setup method
    client = APIClient()

    def test_college(self):
        self.data = {"college_name": "SGSITS", "city": "Indore", "state": "MP"}

        res = self.client.post("/college/", self.data, format="json")
        self.assertEqual(res.status_code, 201)

        res2 = self.client.get("/college/")
        self.assertEqual(res2.status_code, 200)

        res3 = self.client.get(reverse("college", kwargs={"pk": "1"}), self.data)
        self.assertEqual(res3.status_code, 200)

        self.data1 = {"college_name": "LNCT", "city": "Bhopal", "state": "UP"}
        url = reverse('college', args=[res3.data['id']])
        res4 = self.client.put(url, data=self.data1)
        self.assertEqual(res4.status_code, 200)

        res5 = self.client.delete(reverse("college", kwargs={"pk": 1}))
        self.assertEqual(res5.status_code, 200)


class StudentTest(APITestCase):
    request = APIClient()

    def test_student(self):
        self.user = Student.objects.create_user(username='test', password='test123')
        # self.user.set_password('test123')
        # self.user.save()
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        self.college = {"college_name": "SGSITS", "city": "Indore", "state": "MP"}
        self.student = {
            'first_name': 'shivam',
            'last_name': 'singh',
            'username': 'shivam',
            'email': 'shivam@asd.com',
            'branch': 'ex',
            'address': 'bhopal',
            'college': self.college,
            'dob': '1991-08-11'
        }

    # def test_token(self):
        res = self.client.login(username='test', password='test123')
        self.assertTrue(res)

        res1 = self.client.post('/student/', self.student, format='json')
        breakpoint()


# class CreateStudentTest(APITestCase):
#     def setUp(self):
#         self.user = Student.objects.create_user(username='test', password='test123')
#         self.client.login(username='test', password='test123')
#         self.college = {"college_name": "SGSITS", "city": "Indore", "state": "MP"}
#         self.student = {
#             'first_name': 'shivam',
#             'last_name': 'singh',
#             'username': 'shivam',
#             'email': 'shivam@asd.com',
#             'branch': 'ex',
#             'address': 'bhopal',
#             'college': self.college,
#             'dob': '1991-08-11'
#         }
#
#     def test_create(self, **validated_data):
#         self.client.login(username='test', password='test123', **validated_data)
#         res1 = self.client.post('/student/', self.student, format='json')
