# Generated by Django 4.2.4 on 2023-09-06 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TarifaLuz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('1A', '1A'), ('1B', '1B'), ('1C', '1C'), ('1E', '1E'), ('1F', '1F'), ('DAC', 'DAC')], max_length=3)),
                ('ano', models.IntegerField()),
                ('mes', models.CharField(max_length=10)),
                ('consumo_basico', models.DecimalField(decimal_places=3, max_digits=10)),
                ('consumo_intermedio', models.DecimalField(decimal_places=3, max_digits=10)),
                ('consumo_excedente', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
