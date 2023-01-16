from pathlib import Path
from typing import Any, Callable
import threading
import pytube
from controller.on_complete_callback import on_complete_callback as occ
from controller.on_progress_callback import on_progress_callback as opc


def download_audio(
    url: str,
    on_complete_callback: Callable[[Any, bytes, int], None],
    on_progress_callback: Callable[[Any, bytes, int], None]
) -> Path:
    youtube = pytube.YouTube(
        url=url,
        on_complete_callback=on_complete_callback,
        on_progress_callback=on_progress_callback)

    # Select the highest quality audio stream
    audio_stream = youtube.streams.filter(
        only_audio=True).order_by('abr').desc().first()

    # Download the audio stream as an audio file
    download_thread = threading.Thread(target=audio_stream.download)
    download_thread.start()
    print('download_thread started!!!')


if __name__ == '__main__':
    video_url = "https://youtu.be/d0xeShmVx1Q"
    download_audio(video_url, occ, opc)
