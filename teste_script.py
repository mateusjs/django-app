'''
    HEADER DEFAULT PRA QUALQUER SCRIPT QUE UTILIZE UM MODEL DO DJANGO
'''
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crud.settings")
django.setup()
from django.test.utils import setup_test_environment
from django.test import Client
from django.urls import reverse

setup_test_environment()

client = Client()

response = client.get(reverse('polls:index'))
print(response.status_code)
print(response.context['latest_question_list'])