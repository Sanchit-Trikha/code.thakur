# Generated by Django 5.1.6 on 2025-02-14 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_remove_note_file_alter_note_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordedVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('video', models.FileField(upload_to='recorded_videos/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
