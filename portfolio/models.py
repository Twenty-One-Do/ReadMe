from django.db import models
from account.models import User


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

class Link(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    unique_id = models.CharField(max_length=100, unique=True)
    expiration_date = models.DateField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

class Stack(models.Model):
    type_choices = (('Lang', 'Lang'),
                    ('Coop', 'Coop'),
                    ('docs', 'docs'))
    name = models.CharField(max_length=30)
    type = models.CharField(choices=type_choices, max_length=10)

class Stack_Rel(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    stack = models.ForeignKey(Stack, on_delete=models.CASCADE)