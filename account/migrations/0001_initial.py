# Generated by Django 3.2.11 on 2022-01-08 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=20)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.roles')),
            ],
            options={
                'db_table': 'profiles',
            },
        ),
    ]
