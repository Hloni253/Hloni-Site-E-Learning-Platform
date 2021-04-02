# Generated by Django 3.1.4 on 2021-02-08 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_auto_20210207_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='concept',
            name='topic',
        ),
        migrations.AddField(
            model_name='concept',
            name='topic',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Home.topic'),
        ),
        migrations.RemoveField(
            model_name='grade',
            name='subject',
        ),
        migrations.AddField(
            model_name='grade',
            name='subject',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Home.subject'),
        ),
        migrations.RemoveField(
            model_name='topic',
            name='grade',
        ),
        migrations.AddField(
            model_name='topic',
            name='grade',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Home.grade'),
        ),
    ]
