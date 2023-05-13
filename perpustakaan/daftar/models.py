from django.db import models

# Create your models here.

class DaftarSiswa(models.Model) :

    no_anggota_siswa = models.CharField(max_length=10)
    nim = models.CharField(max_length=15)
    nama_anggota = models.CharField(max_length=50)
    jurusan = models.CharField(max_length=20)
    tanggal_lahir = models.DateField()
    alamat = models.TextField()
    kode_pos = models.CharField(max_length=20)
    no_telp = models.CharField(max_length=20)
    tanggal_daftar = models.DateField()

    def __str__(self) :
        return self.no_anggota_siswa