# Generated by Django 4.0.8 on 2023-01-08 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('email', models.TextField(blank=True, null=True)),
                ('feedback', models.TextField()),
                ('rating', models.DecimalField(decimal_places=2, default=99.99, max_digits=15)),
            ],
        ),
    ]