# Generated by Django 3.2.5 on 2022-05-22 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ethnicity',
            field=models.CharField(choices=[('asian', 'Asian'), ('black', 'Black Or African'), ('caucasian', 'Caucasian'), ('hispanic', 'Hispanic Or Latinx'), ('pacific', 'Pacific Islander'), ('omitted', 'Prefer Not To Answer')], default='omitted', max_length=255, verbose_name='Ethnicity'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other'), ('omitted', 'Prefer Not To Answer')], default='omitted', max_length=255, verbose_name='Gender'),
        ),
    ]
