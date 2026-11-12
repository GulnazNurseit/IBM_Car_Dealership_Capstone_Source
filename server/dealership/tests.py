from django.test import TestCase,Client
from django.contrib.auth.models import User
from .models import CarMake,CarModel
class PageTests(TestCase):
    def test_static_pages(self):
        for path in ['/about/','/contact/','/signup/','/login/']:
            self.assertEqual(self.client.get(path).status_code,200)
    def test_models(self):
        make=CarMake.objects.create(name='Demo Motors')
        CarModel.objects.create(make=make,name='Model A',year=2025)
        self.assertEqual(CarModel.objects.count(),1)
    def test_review_requires_login(self):
        self.assertEqual(self.client.get('/dealer/1/review/').status_code,302)
