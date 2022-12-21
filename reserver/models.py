from django.db import models

#Création du model trajet
class Trajet(models.Model):
    depart = models.CharField(max_length=50)
    arrivee= models.CharField(max_length=50)
    def __str__(self):
        return self.depart+ '-' +self.arrivee
    pass


# Création du model Vol
class Vol(models.Model):
    prix = models.FloatField()
    date = models.CharField(max_length = 15 )
    heure = models.CharField(max_length = 5)
    trajet = models.ForeignKey(Trajet , on_delete = models.CASCADE)
    def __str__(self):
        return str(self.prix)
#||||||||||||||||||||||\
#Création du Model Compagnie
class Compagnie(models.Model):
    nom = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="photo/%Y/%m/%d", blank=True)
    vols = models.ManyToManyField(Vol)
    def __str__(self):
        return self.nom

# Create your models here.
