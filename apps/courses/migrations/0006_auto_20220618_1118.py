# Generated by Django 3.2.5 on 2022-06-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_quiz_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizquestion',
            name='quiz',
        ),
        migrations.AddField(
            model_name='quiz',
            name='questions',
            field=models.ManyToManyField(to='courses.QuizQuestion'),
        ),
    ]
