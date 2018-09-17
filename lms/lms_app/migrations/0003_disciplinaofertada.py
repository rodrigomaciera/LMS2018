# Generated by Django 2.0.6 on 2018-09-10 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0002_disciplina'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisciplinaOfertada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.TextField(max_length=255)),
                ('turma', models.TextField(max_length=5)),
                ('ano', models.IntegerField()),
                ('semestre', models.IntegerField()),
                ('professor', models.IntegerField()),
                ('disciplina', models.IntegerField()),
            ],
        ),
    ]
