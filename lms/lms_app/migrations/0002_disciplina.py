# Generated by Django 2.0.6 on 2018-09-10 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(max_length=50)),
                ('ementa', models.TextField(max_length=5000)),
            ],
        ),
    ]
