from django.core.exceptions import ValidationError
from django.db import models

def validate_pdf(file):
    if not file.name.endswith('.pdf'):
        raise ValidationError('Only PDF files are allowed.')

class Note(models.Model):
    title = models.CharField(max_length=200)  
    description = models.TextField()  
    pdf = models.FileField(upload_to='notes_pdfs/', validators=[validate_pdf])  
    uploaded_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.title

class RecordedVideo(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/', blank=True, null=True)  # File upload (optional)
    video_id = models.CharField(max_length=50, unique=True, blank=True, null=True)  # YouTube video ID
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def youtube_url(self):
        if self.video_id:
            return f"https://www.youtube.com/watch?v={self.video_id}"
        return None

class Roadmap(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pdf = models.FileField(upload_to='roadmaps/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
