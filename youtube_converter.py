from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

def get_video_streams(url):
    yt = YouTube(url)
    video_streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    return yt.title, video_streams

def select_resolution(video_streams):
    print("\nAvailable resolutions:")
    unique_resolutions = {}
    for idx, stream in enumerate(video_streams):
        res = stream.resolution
        if res not in unique_resolutions:
            unique_resolutions[res] = idx
            print(f"{len(unique_resolutions)}. {res}")

    choice = int(input("\nEnter the number for your desired resolution: ")) - 1
    selected_res = list(unique_resolutions.values())[choice]
    return video_streams[selected_res]

def download_video(stream, output_path="downloads"):
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

def main():
    url = input("Enter YouTube video URL: ")
    format_choice = input("Convert to (1) MP4 or (2) MP3? Enter 1 or 2: ")

    if format_choice == "1":
        title, streams = get_video_streams(url)
        print(f"\nVideo Title: {title}")
        selected_stream = select_resolution(streams)
        video_path = download_video(selected_stream)
        print(f"Downloaded MP4 to: {video_path}")

    elif format_choice == "2":
        from moviepy.editor import AudioFileClip
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        video_path = stream.download(filename="temp_audio.mp4")
        audio_clip = AudioFileClip(video_path)
        mp3_path = "downloads/" + yt.title.replace(" ", "_") + ".mp3"
        if not os.path.exists("downloads"):
            os.makedirs("downloads")
        audio_clip.write_audiofile(mp3_path)
        audio_clip.close()
        os.remove(video_path)
        print(f"Extracted MP3 to: {mp3_path}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
