# Generated by Django 3.0.8 on 2020-08-29 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_event_poster_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='department',
            field=models.CharField(choices=[('BIOCHEM', 'Biochemistry Section'), ('CHEM', 'Chemistry'), ('COMP', 'Computing'), ('GEO', 'Geography and Geology'), ('LIFE', 'Life Sciences'), ('MATH', 'Mathematics'), ('PHYS', 'Physics'), ('OTHER', 'Other')], max_length=7),
        ),
        migrations.AlterField(
            model_name='geojsonfeature',
            name='associated_with',
            field=models.CharField(choices=[('BIOCHEM', 'Biochemistry Section'), ('CHEM', 'Chemistry'), ('COMP', 'Computing'), ('GEO', 'Geography and Geology'), ('LIFE', 'Life Sciences'), ('MATH', 'Mathematics'), ('PHYS', 'Physics'), ('OTHER', 'Other')], default='OTHER', max_length=7),
        ),
        migrations.AlterField(
            model_name='geometryobject',
            name='geometry_type',
            field=models.CharField(choices=[('Point', 'Point'), ('MultiPoint', 'MultiPoint'), ('LineString', 'LineString'), ('MultiLineString', 'MultiLineString'), ('Polygon', 'Polygon')], max_length=18),
        ),
    ]
