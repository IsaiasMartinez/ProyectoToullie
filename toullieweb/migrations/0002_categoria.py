# Generated by Django 3.1.3 on 2020-11-03 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toullieweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=15)),
                ('activo', models.BooleanField()),
            ],
        ),
    ]
