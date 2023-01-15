from pathlib import Path
import pytube


def download_audio(url: str) -> Path:
    youtube = pytube.YouTube(url)

    audio_stream = youtube.streams.filter(
        only_audio=True).order_by('abr').desc().first()
    print(f'audio_stream = {audio_stream}')
    audio_download_location = audio_stream.download(
        filename=audio_stream.default_filename)

    output_file_path = Path(audio_download_location)
    print(f'Audio has been downloaded to: {output_file_path}')
    return output_file_path


if __name__ == '__main__':
    video_url = "https://youtu.be/qpCNaRkIh2E"
    download_audio(video_url)
