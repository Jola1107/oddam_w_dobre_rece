# Generated by Django 4.1 on 2022-08-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioLab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(null=True)),
                ('type', models.SmallIntegerField(choices=[(0, 'fundacja'), (1, 'organizacja pozarządowa'), (2, 'zbiórka lokalna')], default=0)),
                ('categories', models.ManyToManyField(to='PortfolioLab.category')),
            ],
        ),
    ]
