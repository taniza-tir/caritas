# Generated by Django 3.1.2 on 2020-10-15 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prog_y_proy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('tiempo_eje', models.DateField()),
                ('donante', models.CharField(max_length=40)),
                ('costo', models.IntegerField()),
                ('area_inter', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('tipologia', models.CharField(max_length=100)),
                ('beneficiarios', models.CharField(max_length=40)),
                ('objetivo', models.CharField(max_length=300)),
                ('resul_espera', models.CharField(max_length=400)),
                ('resul_alcan', models.CharField(max_length=400)),
                ('acciones_reali', models.CharField(max_length=400)),
                ('metodo_imple', models.CharField(max_length=200)),
                ('factores_pos', models.CharField(max_length=300)),
                ('factores_neg', models.CharField(max_length=300)),
                ('lecciones_apre', models.CharField(max_length=300)),
                ('creacion', models.DateField(auto_now_add=True)),
                ('actualizacion', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
