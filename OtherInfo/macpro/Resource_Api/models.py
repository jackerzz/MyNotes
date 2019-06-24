from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Foo(models.Model):
    bar = models.CharField(max_length=100)
    owner = models.Foreignkey(User, related_name='foos')

class Bar(models.Model):
    target_type = models.ForeignKey(ContentType)
    target_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_type', 'target_id')
    foo = models.CharField(max_length=100)
    foo1 = models.DecimalField(max_digits=12, decimal_places=5)