from django.db import models

from account.models import User
from portfolio.models import Portfolio


class Post(models.Model):
    type_choices = (('General', 'General'),
                    ('About', 'About'),
                    ('Certificate', 'Certificate'),
                    ('Award', 'Award'),
                    ('Document', 'Document'),)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=5000)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(choices=type_choices, max_length=30)
