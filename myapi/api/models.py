from django.db import models


class Resume(models.Model):

  JUNIOR = 'JR'
  SENIOR = 'SR'
  MIDDLE = 'MD'

  ACTIVE = 'AC'
  INACTIVE = 'IAC'

  GRADES = [
    (JUNIOR, 'Junior'),
    (MIDDLE, 'Middle'),
    (SENIOR, 'Senior')
  ]

  STATUSES = [
    (ACTIVE, 'Active'),
    (INACTIVE, 'Inactive'),
  ]

  grade = models.CharField(max_length=2, choices=GRADES, default=JUNIOR)
  status = models.CharField(max_length=3, choices=STATUSES, default=ACTIVE)
  specialty = models.CharField(max_length=50)
  salary = models.IntegerField()
  education = models.CharField(max_length=50)
  experience = models.CharField(max_length=50)
  portfolio = models.CharField(max_length=50)
  title = models.CharField(max_length=50)
  phone = models.CharField(max_length=50)
  email = models.EmailField()
