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

from student_app.models import College

#from college import student_app


class TestCollegeView(unittest.TestCase):
    @patch('student_app.services')
    def test_college_post(self, request):
        clg = request

        clg.post = {
            'college_name': 'SGSITS',
            'city': 'indore',
            'state': 'mp'
        }

        res = clg.post
        self.assertIsNotNone(res)
        self.assertIsInstance(res, dict)

        breakpoint()
