# Generated by Django 4.2.3 on 2023-08-29 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio_app', '0006_remove_paciente_contrasena1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='username',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
