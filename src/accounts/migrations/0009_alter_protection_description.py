# Generated by Django 3.2.5 on 2021-11-09 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20211108_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protection',
            name='description',
            field=models.CharField(max_length=999, null=True),
        ),
    ]
