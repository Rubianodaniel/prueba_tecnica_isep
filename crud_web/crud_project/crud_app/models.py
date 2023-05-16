from django.db import models


class Validate(models.Model):
    numeric_field1 = models.IntegerField()
    numeric_field2 = models.IntegerField()
    numeric_field3 = models.IntegerField()
    text_field1 = models.TextField()
    text_field2 = models.TextField()
    date_field = models.DateField()