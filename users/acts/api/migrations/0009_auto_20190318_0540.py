# Generated by Django 2.1.7 on 2019-03-18 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190213_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act',
            name='username',
            field=models.TextField(),
        ),
    ]
