# Generated by Django 3.1.4 on 2021-02-07 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DefinitionsAndExplanations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='explanationlinks',
            name='explanation',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='DefinitionsAndExplanations.explanation'),
        ),
    ]