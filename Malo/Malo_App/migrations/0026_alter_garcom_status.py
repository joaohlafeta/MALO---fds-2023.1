# Generated by Django 4.2 on 2023-05-23 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Malo_App', '0025_garcom_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garcom',
            name='status',
            field=models.CharField(blank=True, choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')], max_length=8, null=True, verbose_name='Status'),
        ),
    ]
