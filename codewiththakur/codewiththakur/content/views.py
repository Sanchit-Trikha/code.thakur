from django.shortcuts import render
import requests
from django.conf import settings
from .models import Note, RecordedVideo, Roadmap

# ✅ Home Page View
def home_view(request):
    return render(request, 'home.html')

# ✅ Notes Page View
def notes_view(request):
    notes = Note.objects.all()
    return render(request, 'notes.html', {'notes': notes})

# ✅ About Page View
def about_view(request):
    return render(request, 'about.html')

# ✅ Roadmap Page View
def roadmap_list(request):
    roadmaps = Roadmap.objects.all()
    return render(request, 'roadmap.html', {'roadmaps': roadmaps})

# ✅ YouTube Videos Fetch Karne Ka Function
def fetch_youtube_videos():
    api_key = settings.YOUTUBE_API_KEY  # API Key ko settings se le rahe hain
    channel_id = "UC0gZFqhUEDs_PBO1LrOB33Q"  # Aapka YouTube Channel ID
    url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=10"
    
    response = requests.get(url)
    data = response.json()

    if "items" in data:
        for item in data["items"]:
            if "videoId" in item["id"]:  # ✅ Ensure 'videoId' exists
                video_id = item["id"]["videoId"]
                title = item["snippet"]["title"]
                published_at = item["snippet"]["publishedAt"]

                # ✅ Check if video already exists before adding
                if not RecordedVideo.objects.filter(video_id=video_id).exists():
                    RecordedVideo.objects.create(
                        title=title,
                        video_id=video_id,
                        published_at=published_at
                    )

# ✅ Recorded Videos Page View
def recorded_videos_view(request):
    fetch_youtube_videos()  # ✅ YouTube se latest videos fetch karna
    videos = RecordedVideo.objects.all().order_by("-published_at")  # ✅ Newest First
    return render(request, 'recorded_videos.html', {'videos': videos})
