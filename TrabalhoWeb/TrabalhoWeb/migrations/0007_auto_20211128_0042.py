# Generated by Django 3.2.9 on 2021-11-28 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrabalhoWeb', '0006_auto_20211128_0018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=1, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario',
            field=models.CharField(help_text='Usuario', max_length=100, primary_key=True, serialize=False),
        ),
    ]