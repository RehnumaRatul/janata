# Generated by Django 4.0.3 on 2022-03-22 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0003_alter_visualdata_close_alter_visualdata_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visualdata',
            name='date',
            field=models.CharField(max_length=10000),
        ),
    ]
