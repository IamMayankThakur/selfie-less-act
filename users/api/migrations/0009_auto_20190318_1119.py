# Generated by Django 2.1.7 on 2019-03-18 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190213_1058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='act',
            name='category',
        ),
        migrations.RemoveField(
            model_name='act',
            name='username',
        ),
        migrations.DeleteModel(
            name='Act',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
