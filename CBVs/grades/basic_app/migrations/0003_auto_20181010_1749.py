# Generated by Django 2.1.1 on 2018-10-10 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20181010_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='candidate',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='basic_app.SiteUser'),
        ),
    ]
