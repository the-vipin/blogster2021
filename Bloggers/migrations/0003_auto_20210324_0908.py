# Generated by Django 3.1.7 on 2021-03-24 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bloggers', '0002_auto_20210324_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogger',
            name='About',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
