# Generated by Django 2.1.5 on 2019-02-11 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_act_actid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='act',
            name='actId',
        ),
        migrations.AlterField(
            model_name='act',
            name='upvote',
            field=models.IntegerField(),
        ),
    ]
