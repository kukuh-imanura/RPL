# Generated by Django 4.2.1 on 2023-05-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petugas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabelpetugas',
            name='kodePetugas',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
