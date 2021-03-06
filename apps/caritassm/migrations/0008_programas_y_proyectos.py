# Generated by Django 3.1.2 on 2020-10-16 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caritassm', '0007_delete_prog_y_proy'),
    ]

    operations = [
        migrations.CreateModel(
            name='programas_y_proyectos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('costo', models.IntegerField()),
                ('area_intervencion', models.CharField(max_length=800)),
                ('beneficiarios', models.CharField(max_length=200)),
                ('objetivo', models.CharField(max_length=800)),
                ('resultados_esperados', models.CharField(max_length=900)),
                ('resultados_alcanzados', models.CharField(max_length=900)),
                ('acciones_realizadas', models.CharField(max_length=1000)),
                ('metodo_implementado', models.CharField(max_length=1000)),
                ('factores_positivos', models.CharField(max_length=1000)),
                ('factores_negativos', models.CharField(max_length=1000)),
                ('lecciones_aprendidas', models.CharField(max_length=1200)),
                ('creacion', models.DateField(auto_now_add=True)),
                ('actualizacion', models.DateField(auto_now_add=True)),
                ('donante', models.ManyToManyField(to='caritassm.donantes')),
                ('municipio', models.ManyToManyField(to='caritassm.municipios')),
                ('tipologia', models.ManyToManyField(to='caritassm.tipologia')),
            ],
        ),
    ]
