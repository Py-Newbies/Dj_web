import uuid
from datetime import datetime

import pycountry
from django.db import models


# reset id column - UPDATE sqlite_sequence SET seq = 0 WHERE sqlite_sequence.name = "students";
class Student(models.Model):
    name = models.CharField(max_length=100)
    token = models.CharField(max_length=50, default=uuid.uuid4, editable=False)
    mobile_num = models.CharField(max_length=10, unique=True)
    country = models.CharField(max_length=50, choices=[(i.name, i.name) for i in list(pycountry.countries)],
                               default='United States')
    visa_type = models.CharField(max_length=10, choices=[('Study', 'Study'), ('Work', 'work')], default='Study')
    created_by = models.CharField(max_length=100)
    created_date = models.DateField(default=datetime.now().date())

    class Meta:
        db_table = "students"
