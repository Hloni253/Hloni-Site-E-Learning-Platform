# Generated by Django 3.1.4 on 2021-02-06 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='image_url',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
        migrations.DeleteModel(
            name='SubjectImage',
        ),
    ]
