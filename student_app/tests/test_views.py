# import unittest import mock
# from django.test import RequestFactory
# from django.urls import reverse
# from student_app.models import College
# from student_app.views import CollegeView


# class CollegeViewTest(unittest.TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.college = {
#             'college_name': 'SGSITS',
#             'city': 'indore',
#             'state': 'mp'
#         }
#
#     def test_post(self):
#         request = self.factory.post('/college/')
#         response = CollegeView.as_view()(request, self.college)




import unittest
from unittest import TestCase
from unittest.mock import patch, Mock

from student_app.services import CollegeService

from student_app.models import College

#from college import student_app
from student_app import services



class TestCollegeView(unittest.TestCase):
    @patch('student_app.views.CollegeView.post')
    def test_college_post(self, clg):
        clg.post = {
            'college_name': 'SGSITS',
            'city': 'indore',
            'state': 'mp'
        }
        breakpoint()

        res = clg.post
        self.assertIsNotNone(res)
        self.assertIsInstance(res, dict)


