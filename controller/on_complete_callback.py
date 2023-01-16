from pathlib import Path
import pytube
from controller.extract_bitrate import extract_bitrate
from controller.convert_audio_format import convert_audio_format


def on_complete_callback(stream: pytube.Stream, file_path: str) -> None:
    """
    Callback function that is executed when the audio stream download is complete.

    This function takes the following parameters:
    stream (pytube.Stream) : The audio stream that was downloaded.
    file_path (str) : The file path where the audio stream was downloaded to.

    This function does not return anything.
    """
    print(f'Audio stream: {stream}\nhas been downloaded to: {file_path}')

    # Call the convert_audio_format function
    input_file_path = Path(file_path)
    output_file_path = input_file_path.with_suffix('.mp3')
    audio_bitrate = extract_bitrate(stream.abr)
    convert_audio_format(input_file_path, output_file_path, audio_bitrate)
