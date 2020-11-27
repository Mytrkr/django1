from django.db import models

class competitor(models.Model):
	tcNumber = models.CharField(max_length = 75, verbose_name = "TC No")
	name = models.CharField(max_length = 75, verbose_name = "Ad")
	surname = models.CharField(max_length = 75, verbose_name = "Soyad")
	school = models.CharField(max_length = 75, verbose_name = "Okul")
	faculty = models.CharField(max_length = 75, verbose_name = "Bölüm")

	compeleted = models.BooleanField(verbose_name = "Durum")

	def __str__(self):
		return self.tcNumber

class competition(models.Model):
	competitionName = models.CharField(max_length = 100, verbose_name = "Yarışma Adı")
	competitionComment = models.CharField(max_length = 500, verbose_name = "Yarışma Açıklaması")

	def __str__(self):
		return self.competitionName