from pathlib import Path
import threading
import pytube


def on_complete_callback(stream, file_path) -> None:
    """Callback function prints message"""
    print(f'Audio stream: {stream}\nhas been downloaded to: {file_path}')


def on_progress_callback(stream, chunk, bytes_remaining) -> None:
    """Callback function when there is progress"""
    total_bytes = stream.filesize
    completed_bytes = total_bytes - bytes_remaining
    percentage_completed = (completed_bytes / total_bytes) * 100

    print(f"""Progress = {percentage_completed:.2f}%""")


def download_audio(url: str, on_complete_callback, on_progress_callback) -> Path:
    youtube = pytube.YouTube(
        url,
        on_complete_callback=on_complete_callback,
        on_progress_callback=on_progress_callback)

    audio_stream = youtube.streams.filter(
        only_audio=True).order_by('abr').desc().first()

    # Download the audio file
    download_thread = threading.Thread(target=audio_stream.download)
    download_thread.start()
    print('download_thread started!!!')


if __name__ == '__main__':
    video_url = "https://youtu.be/d0xeShmVx1Q"
    download_audio(video_url, on_complete_callback, on_progress_callback)
