# Generated by Django 3.2.7 on 2021-09-30 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0013_alter_complaints_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='lat',
            field=models.DecimalField(decimal_places=6, default='10.2345', max_digits=18),
        ),
    ]
