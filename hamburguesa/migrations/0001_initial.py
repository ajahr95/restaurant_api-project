# Generated by Django 3.0.5 on 2020-04-28 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hamburguesa',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=500)),
                ('imagen', models.URLField()),
            ],
        ),
    ]
