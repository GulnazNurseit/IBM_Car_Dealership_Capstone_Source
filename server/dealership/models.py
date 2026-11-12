from django.db import models
class CarMake(models.Model):
    name=models.CharField(max_length=120,unique=True)
    def __str__(self): return self.name
class CarModel(models.Model):
    make=models.ForeignKey(CarMake,related_name='models',on_delete=models.CASCADE)
    name=models.CharField(max_length=120)
    year=models.PositiveIntegerField()
    category=models.CharField(max_length=60,default='Sedan')
    def __str__(self): return f'{self.make.name} {self.name} ({self.year})'
    class Meta:
        constraints=[models.UniqueConstraint(fields=['make','name','year'],name='unique_car_model')]
