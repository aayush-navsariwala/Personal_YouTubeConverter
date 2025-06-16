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

def convert_to_mp3(video_path):
    mp3_path = os.path.splitext(video_path)[0] + ".mp3"
    video = AudioFileClip(video_path)
    video.write_audiofile(mp3_path)
    video.close()
    return mp3_path
