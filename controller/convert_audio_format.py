from pydub import AudioSegment
import threading


def convert_audio_format(input_file: str, output_file: str, abr: str) -> None:
    """
    This function converts an audio file from webm format to mp3 format and limits the bitrate to the given value.
    It uses the pydub library and a threading.Thread to execute the conversion.

    Args:
    input_file (str): The path to the input file.
    output_file (str): The path to the output file.
    abr (str): The desired bitrate for the output file.

    """
    sound = AudioSegment.from_file(input_file, format="webm")
    print(f'abr = {abr}')

    # Use export() method to convert the file to MP3 format
    convert_thread = threading.Thread(
        target=sound.export, args=(output_file,), kwargs={"format": "mp3", "bitrate": abr})
    convert_thread.start()

    print('convert_thread started!!!')
