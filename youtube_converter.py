from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

def download_video(url, output_path="downloads"):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    video_path = stream.download(output_path=output_path)
    return video_path
