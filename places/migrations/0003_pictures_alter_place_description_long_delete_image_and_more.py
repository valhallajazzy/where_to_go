# Generated by Django 4.2.6 on 2023-10-30 20:56

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_alter_image_options_alter_image_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(default=0, verbose_name='Позиция')),
                ('image', models.ImageField(blank=True, null=True, unique=True, upload_to='', verbose_name='Картинка')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(verbose_name='Развернутое описание'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='pictures',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place'),
        ),
    ]
