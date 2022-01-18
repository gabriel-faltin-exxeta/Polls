# Generated by Django 3.2.9 on 2022-01-18 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_choice_question'),
        ('users', '0003_alter_customuser_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='choice',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.choice'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='question',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.question'),
        ),
    ]
