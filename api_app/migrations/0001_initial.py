# Generated by Django 2.2.4 on 2020-01-16 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('disc', models.TextField(null=True, verbose_name='discription')),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.TextField(verbose_name='question')),
                ('answer', models.TextField(verbose_name='answer')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.Quiz')),
            ],
        ),
    ]
