# Generated by Django 3.2.9 on 2022-05-25 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='regression_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_val', models.DecimalField(decimal_places=3, max_digits=6)),
                ('y_val', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
        ),
    ]
