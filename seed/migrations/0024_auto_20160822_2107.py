# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-23 04:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0023_auto_20160822_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxlotauditlog',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taxlotauditlog__child', to='seed.TaxLotAuditLog'),
        ),
        migrations.AlterField(
            model_name='taxlotauditlog',
            name='parent1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taxlotauditlog__parent1', to='seed.TaxLotAuditLog'),
        ),
        migrations.AlterField(
            model_name='taxlotauditlog',
            name='parent2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taxlotauditlog__parent2', to='seed.TaxLotAuditLog'),
        ),
    ]
