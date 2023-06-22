# Generated by Django 4.2.1 on 2023-06-22 17:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('run', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1000000), django.core.validators.MaxValueValidator(99999999)])),
                ('dv', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('0', '0'), ('K', 'K')], max_length=1)),
                ('primer_nombre', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-ZñÑ]*$', 'Ingrese solo letras')])),
                ('segundo_nombre', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-ZñÑ]*$', 'Ingrese solo letras')])),
                ('apellido_paterno', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-ZñÑ]*$', 'Ingrese solo letras')])),
                ('apellido_materno', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-ZñÑ]*$', 'Ingrese solo letras')])),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id_habitacion', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('cant_camas', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('cant_banos', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('estado_habitacion', models.CharField(choices=[('D', 'Disponible'), ('ND', 'No disponible')], max_length=15)),
                ('hotel', models.CharField(choices=[('H1', 'Hotel 1'), ('H2', 'Hotel 2')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_habitacion',
            fields=[
                ('id_tipo_habitacion', models.AutoField(primary_key=True, serialize=False)),
                ('nom_tipo', models.CharField(max_length=50, unique=True)),
                ('descrip_tipo', models.TextField(null=True)),
                ('precio', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_reservacion', models.DateField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('total_reserva', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.habitacion')),
                ('run_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='habitacion',
            name='tipo_habitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tipo_habitacion'),
        ),
    ]
