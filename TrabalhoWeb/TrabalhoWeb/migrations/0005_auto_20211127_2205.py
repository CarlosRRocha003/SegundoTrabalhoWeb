# Generated by Django 3.2.7 on 2021-11-28 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrabalhoWeb', '0004_remove_usuario_senha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario',
            field=models.CharField(help_text='Usuario', max_length=100, primary_key=True, serialize=False),
        ),
    ]
