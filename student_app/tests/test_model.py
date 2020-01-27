import unittest

import factory
from .factories import CollegeFactory, StudentFactory


class TestCollegeModel(unittest.TestCase):
    def test_college_factory(self):
        college_factory = CollegeFactory(college_name='SGSITS',
                                         city='Indore',
                                         state='MP')

        self.assertEqual(college_factory.college_name, 'SGSITS')
        self.assertEqual(college_factory.city, 'Indore')
        self.assertEqual(college_factory.state, 'MP')


class TestStudentModel(unittest.TestCase):
    def test_student_factory(self):
        clg_inst = CollegeFactory(college_name='SGSITS',
                                  city='Indore',
                                  state='MP')


        student_factory = StudentFactory(first_name='shivam',
                                         last_name='singh',
                                         username='shivam',
                                         email='shivam@asd.com',
                                         branch='ex',
                                         address='bhopal',
                                         college=clg_inst,
                                         dob='1991-08-11')

        self.assertEqual(student_factory.first_name, 'shivam')
        self.assertEqual(student_factory.last_name, 'singh')
        self.assertEqual(student_factory.username, 'shivam')
        self.assertEqual(student_factory.email, 'shivam@asd.com')
        self.assertEqual(student_factory.branch, 'ex')
        self.assertEqual(student_factory.college, clg_inst)
        self.assertEqual(student_factory.dob, '1991-08-11')
        self.assertTrue(student_factory.has_usable_password())



