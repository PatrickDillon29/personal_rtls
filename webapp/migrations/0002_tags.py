# Generated by Django 3.1.7 on 2021-04-18 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tags',
            fields=[
                ('tag_id', models.IntegerField(primary_key=True, serialize=False)),
                ('tag_zone', models.IntegerField()),
                ('x_pos', models.DecimalField(decimal_places=2, max_digits=4)),
                ('y_pos', models.DecimalField(decimal_places=2, max_digits=4)),
                ('z_pos', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]