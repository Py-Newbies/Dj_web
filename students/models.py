import uuid
from django.db import models


# reset id column - UPDATE sqlite_sequence SET seq = 0 WHERE sqlite_sequence.name = "students";
class Student(models.Model):
    name = models.CharField(max_length=100)
    # first_name = models.CharField(max_length=255, blank=True)
    # last_name = models.CharField(max_length=255, blank=True)
    token = models.CharField(max_length=50, default=uuid.uuid4, editable=False)
    mobile_num = models.CharField(max_length=10, unique = True)

    class Meta:
        db_table = "students"
