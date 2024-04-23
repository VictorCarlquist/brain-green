from django.db import models


class Producer(models.Model):
    cpf_cnpj = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Farm(models.Model):
    # Farm model with city, state, total area, arable area, vegetation area, and crops
    producer = models.ForeignKey('Producer', on_delete=models.CASCADE)
    farm_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    total_area_hectares = models.FloatField()

    def __str__(self):
        return self.producer.farm_name


class AreaFarm(models.Model):
    # AreaFarm model with farm, area type, area in hectares, and area in percentage
    farm = models.ForeignKey('Farm', on_delete=models.CASCADE)
    AREA_CHOICES = [
        ('AR', 'Arable'),
        ('VE', 'Vegetation'),
    ]
    area_type = models.CharField(max_length=2, choices=AREA_CHOICES)
    area_hectares = models.FloatField()
    CROPS_CHOICES = [
        ('SO', 'Soja'),
        ('MI', 'Milho'),
        ('AL', 'Algodão'),
        ('CA', 'Café'),
        ('CS', 'Cana de Açucar'),
    ]
    crops = models.CharField(max_length=2, choices=CROPS_CHOICES)

    def __str__(self):
        return self.area_type
