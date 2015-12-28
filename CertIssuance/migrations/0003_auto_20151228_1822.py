# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 18:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CertIssuance', '0002_auto_20151228_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='PinNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=50)),
                ('generated_for_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CertIssuance.User')),
            ],
        ),
        migrations.CreateModel(
            name='RemoteService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(protocol='IPv4')),
                ('port', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='defaultcertificateauthority',
            name='id',
        ),
        migrations.RemoveField(
            model_name='defaultcertificateauthority',
            name='ip_address',
        ),
        migrations.RemoveField(
            model_name='defaultcertificateauthority',
            name='port',
        ),
        migrations.AddField(
            model_name='issuedcertificate',
            name='base64_certificate',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='DirectoryServer',
            fields=[
                ('remoteservice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='CertIssuance.RemoteService')),
                ('name', models.CharField(max_length=50)),
            ],
            bases=('CertIssuance.remoteservice',),
        ),
        migrations.AddField(
            model_name='defaultcertificateauthority',
            name='remoteservice_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='CertIssuance.RemoteService'),
            preserve_default=False,
        ),
    ]
