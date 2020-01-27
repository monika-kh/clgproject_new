import datetime

import factory
import factory.fuzzy

from student_app.models import College, Student


class CollegeFactory(factory.Factory):
    class Meta:
        model = College

    college_name = factory.fuzzy.FuzzyText(length=200)
    city = factory.fuzzy.FuzzyText(length=200)
    state = factory.fuzzy.FuzzyText(length=200)


class StudentFactory(factory.Factory):
    class Meta:
        model = Student
    first_name = factory.fuzzy.FuzzyText(length=30)
    last_name = factory.fuzzy.FuzzyText(length=150)
    username = factory.fuzzy.FuzzyText(length=30)
    email = factory.fuzzy.FuzzyText(length=150)
    branch = factory.fuzzy.FuzzyText(length=30)
    address = factory.fuzzy.FuzzyText(length=150)
    college = factory.SubFactory(CollegeFactory)
    dob = factory.fuzzy.FuzzyDate(datetime.date(1900, 1, 1))




