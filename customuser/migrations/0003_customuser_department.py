# Generated by Django 4.1.4 on 2023-02-23 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0002_alter_customuser_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='department',
            field=models.CharField(default='admin', max_length=255),
            preserve_default=False,
        ),
    ]
