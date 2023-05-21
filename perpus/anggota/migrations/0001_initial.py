# Generated by Django 4.2.1 on 2023-05-21 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='anggotaSiswa',
            fields=[
                ('no_anggota', models.AutoField(primary_key=True, serialize=False)),
                ('nim', models.CharField(max_length=15)),
                ('nama', models.CharField(max_length=50)),
                ('jurusan', models.CharField(max_length=20)),
                ('tanggal_lahir', models.DateField()),
                ('alamat', models.CharField(max_length=50)),
                ('kode_post', models.CharField(max_length=20)),
                ('hp', models.CharField(max_length=20)),
            ],
        ),
    ]