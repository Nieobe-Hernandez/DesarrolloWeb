# Generated by Django 5.1.4 on 2025-04-24 03:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorías', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetallesProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=300)),
                ('fecha_caducidad', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('contacto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('imagen', models.URLField()),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categorías.categoria')),
                ('detalles_producto', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.detallesproducto')),
                ('proveedor', models.ManyToManyField(to='productos.proveedor')),
            ],
        ),
    ]
