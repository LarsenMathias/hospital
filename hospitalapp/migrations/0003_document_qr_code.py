# Generated by Django 4.1.3 on 2023-06-07 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0002_alter_document_file_alter_document_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]