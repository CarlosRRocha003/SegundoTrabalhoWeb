# Generated by Django 3.2.7 on 2021-11-28 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TrabalhoWeb', '0003_alter_candidato_dtnasc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='senha',
        ),
    ]