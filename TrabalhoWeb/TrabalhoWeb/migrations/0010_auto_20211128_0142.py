# Generated by Django 3.2.7 on 2021-11-28 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrabalhoWeb', '0009_auto_20211128_0132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='id',
        ),
        migrations.AddField(
            model_name='empresa',
            name='usuario',
            field=models.CharField(default=1, help_text='Nome', max_length=100, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
