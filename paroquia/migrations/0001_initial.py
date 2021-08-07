# Generated by Django 3.1.7 on 2021-08-06 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paroquia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Nome da Paróquia')),
            ],
            options={
                'verbose_name': 'Paróquia',
                'verbose_name_plural': 'Paróquias',
                'ordering': ['name'],
            },
        ),
    ]
