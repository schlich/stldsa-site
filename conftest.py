from stl_dsa.users.models import User
import pytest
from django.contrib.auth.models import Group
from stl_dsa.users.tests.factories import UserFactory
from model_bakery import baker


# @pytest.fixture
# def nonuser():
#     return baker.make("Person")


# @pytest.fixture
# def nonmember_person():
#     return baker.make("Person")


# @pytest.fixture
# def member_person(db):
#     person = baker.prepare("Person")
#     person.id = 1
#     person.tags.set("Voting Members")
#     return person


# @pytest.fixture
# def user(nonmember_person):
#     user = UserFactory.build()
#     user.person = nonmember_person
#     return user


# @pytest.fixture
# def member(member_person):
#     user = UserFactory.build()
#     user.person = member_person
#     return user