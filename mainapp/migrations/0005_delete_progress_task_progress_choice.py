# Generated by Django 4.0.3 on 2022-03-14 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_progress_remove_task_progress_choice'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Progress',
        ),
        migrations.AddField(
            model_name='task',
            name='progress_choice',
            field=models.CharField(blank=True, choices=[('Need_to_do', 'Need To Do'), ('In_progress', 'In Progress'), ('Finish', 'Finish')], max_length=15),
        ),
    ]