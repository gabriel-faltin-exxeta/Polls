# Generated by Django 3.2.9 on 2021-12-13 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('pages', '0004_contactpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='ContactPage',
        ),
    ]
