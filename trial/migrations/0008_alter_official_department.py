# Generated by Django 3.2.7 on 2021-09-29 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0007_complaints_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='official',
            name='department',
            field=models.CharField(choices=[('W', 'Water'), ('E', 'Electricity'), ('R', 'Roads')], max_length=1),
        ),
    ]