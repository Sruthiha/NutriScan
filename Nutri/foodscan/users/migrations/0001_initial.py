# Generated by Django 4.2.7 on 2025-02-16 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bp', models.CharField(blank=True, max_length=10, null=True)),
                ('sugar', models.CharField(blank=True, max_length=10, null=True)),
                ('cholesterol', models.CharField(blank=True, max_length=10, null=True)),
                ('weight', models.CharField(blank=True, max_length=10, null=True)),
                ('height', models.CharField(blank=True, max_length=10, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('health_issues', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
