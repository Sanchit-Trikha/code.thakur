# Generated by Django 5.1.6 on 2025-02-15 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_alter_recordedvideo_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roadmap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pdf', models.FileField(upload_to='roadmaps/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
