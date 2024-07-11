# Generated by Django 5.0.6 on 2024-07-11 02:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0004_lenguaje'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lenguaje',
            name='id',
        ),
        migrations.AddField(
            model_name='lenguaje',
            name='idlenguaje',
            field=models.AutoField(db_column='id_lenguaje', default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postulacion',
            name='id_lenguaje',
            field=models.ForeignKey(db_column='id_lenguaje', default=1, on_delete=django.db.models.deletion.CASCADE, to='mi_app.lenguaje'),
            preserve_default=False,
        ),
    ]
