from pathlib import Path
import threading
import pytube
from pydub import AudioSegment


def extract_bitrate(bitrate: str) -> str:
    return bitrate.rstrip('bps')


def convert_audio_format(input_file: str, output_file: str, abr: str):
    sound = AudioSegment.from_file(input_file, format="webm")
    print(f'abr = {abr}')

    # Use export() method to convert the file to MP3 format
    convert_thread = threading.Thread(
        target=sound.export, args=(output_file,), kwargs={"format": "mp3", "bitrate": abr})
    convert_thread.start()

    print('convert_thread started!!!')


def on_complete_callback(stream, file_path) -> None:
    """Callback function prints message"""
    print(f'Audio stream: {stream}\nhas been downloaded to: {file_path}')

    # Call the convert_audio_format function
    input_file_path = Path(file_path)
    output_file_path = input_file_path.with_suffix('.mp3')
    audio_bitrate = extract_bitrate(stream.abr)
    convert_audio_format(input_file_path, output_file_path, audio_bitrate)


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
