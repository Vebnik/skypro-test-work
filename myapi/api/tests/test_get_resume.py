from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Resume


class ResumePatchTest(APITestCase):

  @classmethod
  def setUpTestData(cls) -> None:
    Resume(**{
      "grade": "JR",
      "status": "AC",
      "specialty": "Python web dev",
      "salary": 76000,
      "education": "Some edu",
      "experience": "1 years",
      "portfolio": "https://some_portfolio_url.com",
      "title": "Python Django developer",
      "phone": "+7 (924) 700-70-04",
      "email": "vebnik111@gmail.com"
    }).save()

  def test_patch_data(self):

      url = 'http://127.0.0.1:8080/api/resume/'
      response = self.client.get(url, format='json')

      self.assertEqual(response.status_code, 200)
      self.assertEqual(Resume.objects.count(), 1)
      self.assertEqual(Resume.objects.get().salary, 76000)