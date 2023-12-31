# Generated by Django 4.2.2 on 2023-07-07 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0003_docente_jornada_docente_sexo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Universidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='docente',
            name='universidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='docentes.universidad'),
        ),
    ]
