from django.db import models

# Create your models here.


class RumahSakit(models.Model):
    nama = models.CharField(max_length=40)
    alamat = models.CharField(max_length=60)
    kapasitas = models.IntegerField()
    isi = models.IntegerField()
    telp = models.CharField(max_length=25)

    kode_lokasi = models.CharField(max_length=6)

    def __str__(self):
        return self.nama

    def tambah_kapasitas(self):
        self.isi += 1

    def cek_penuh(self):
        return isi >= kapasitas


class BedRequest(models.Model):
    GENDER = (('L', 'Laki-laki'), ('P', 'Perempuan'))

    rs = models.ForeignKey(RumahSakit, on_delete=models.CASCADE, null=True)
    nama = models.CharField(max_length=40)
    alamat = models.CharField(max_length=60)
    gender = models.CharField(max_length=1, choices=GENDER, default='L')
    umur = models.IntegerField()
    telp = models.CharField(max_length=15)
