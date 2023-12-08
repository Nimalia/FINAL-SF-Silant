# Generated by Django 4.2.7 on 2023-11-30 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicecompany',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Сервисная компания'),
        ),
        migrations.AddField(
            model_name='client',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Клиент'),
        ),
        migrations.AddField(
            model_name='claim',
            name='description_failure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reason_refusal', to='app.descriptionfailure', verbose_name='Описание отказа'),
        ),
        migrations.AddField(
            model_name='claim',
            name='failure_node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='failure_node', to='app.failurenode', verbose_name='Узел отказа'),
        ),
        migrations.AddField(
            model_name='claim',
            name='recovery_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recovery_method', to='app.recoverymethod', verbose_name='Способ восстановления'),
        ),
        migrations.AddField(
            model_name='claim',
            name='service_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.servicecompany', verbose_name='Сервисная компания'),
        ),
        migrations.AddField(
            model_name='claim',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.vehicle', verbose_name='Техника'),
        ),
    ]
