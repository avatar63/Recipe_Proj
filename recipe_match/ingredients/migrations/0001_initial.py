# Generated by Django 4.1.5 on 2023-03-05 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_queries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('ingredients', models.CharField(max_length=40000)),
                ('recipe_count', models.CharField(max_length=3)),
            ],
        ),
    ]
