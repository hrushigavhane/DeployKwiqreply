# Generated by Django 3.0.7 on 2021-05-15 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywork', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business_profile',
            name='business_number',
            field=models.CharField(default=91123456879, max_length=15),
        ),
    ]
