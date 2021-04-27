# Generated by Django 3.1.7 on 2021-04-22 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_remove_tag_table_z_pos'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag_table',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag_table',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
