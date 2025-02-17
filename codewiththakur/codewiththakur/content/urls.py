from django.urls import path
from .views import home_view, notes_view, recorded_videos_view,  roadmap_list  

urlpatterns = [
    path('', home_view, name='home'),
    path('notes/', notes_view, name='notes'),
    path('recorded-videos/', recorded_videos_view, name='recorded_videos'),  # Corrected
    path('roadmap/', roadmap_list, name='roadmap'),
]



