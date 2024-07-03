from django.db import models
from django.core.exceptions import ValidationError
import string

# Models de ultrasaga


def valida_nif(value):
    if len(value) != 8:
        raise ValidationError('El Nif ha de ser de 8 dígits')
    if value[0] not in string.ascii_letters:
        raise ValidationError('El primer caràcter del NIF ha de ser una lletra.')


class Escola(models.Model):

    nom = models.CharField(max_length=100)
    nif = models.CharField(
        max_length=8,
        validators = [valida_nif],
        blank=False,
        null=False)
    nif_titular = models.CharField(
        max_length=8,
        validators = [valida_nif],
        blank=False,
        null=False)
    codi_centre = models.CharField(
        max_length=8,
        blank=False,
        null=False)

    def __str__(self):
        return f"{self.nom} {self.nif} {self.nif_titular} {self.codi_centre} "


class Estudi(models.Model):
    nom = models.CharField(
        max_length=100,
        null=False,
        blank=False)
    codi = models.CharField(
        max_length=20,
        null=False,
        blank=False)
    normativa = models.TextField(
        null=True)
    link = models.CharField(
        max_length=200,
        null=True)

    estudis = models.ManyToManyField('Estudi', through='Oferta')

    def __str__(self):
        return f"{self.nom} {self.codi} {self.normativa} {self.link}"


class Oferta(models.Model):
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    estudi = models.ForeignKey(Estudi, on_delete=models.CASCADE)
    any_oferta = models.IntegerField()

    def __str__(self):
        return f"{self.escola} ofereix {self.estudi} des de {self.any_oferta}"


class Modul(models.Model):

    estudi = models.ForeignKey(Estudi, on_delete=models.CASCADE)

    nom = models.CharField(
        max_length=100,
        null=False,
        blank=False)
    codi = models.CharField(
        max_length=8,
        default='00000001')
    codi = models.CharField(
        max_length=8,
        default='00000001')

    def __str__(self):
        return f"{self.nom} {self.codi}"


class Uf(models.Model):
    nom = models.CharField(
        max_length=100,
        null=False,
        blank=False)
    codi = models.CharField(
        max_length=8,
        null=False,
        blank=False)
    duracio = models.IntegerField(
        blank=False,
        null=False)
    ects = models.IntegerField(
        blank=False,
        null=False)


    def __str__(self):
        return f"{self.nom} {self.codi} {self.ects}"


class Ra(models.Model):
    resultat_aprenentatge = models.TextField()

    def __str__(self):
       return f"{self.resultat_aprenentatge}"

class Ca(models.Model):
    criteri_avaluacio = models.TextField()

    def __str__(self):
        return f"{self.criteri_avaluacio}"

class Contingut(models.Model):
    contingut = models.TextField()

    def __str__(self):
       return f"{self.contingut}"


