from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name='CarMake', fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('name',models.CharField(max_length=120,unique=True))]),
        migrations.CreateModel(name='CarModel',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('name',models.CharField(max_length=120)),('year',models.PositiveIntegerField()),('category',models.CharField(default='Sedan',max_length=60)),('make',models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name='models',to='dealership.carmake'))]),
        migrations.AddConstraint(model_name='carmodel', constraint=models.UniqueConstraint(fields=('make','name','year'),name='unique_car_model')),
    ]
