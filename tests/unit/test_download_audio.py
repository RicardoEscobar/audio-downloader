"""Test the download_audio module"""
import unittest
import pytube
from download_audio import download_audio


class TestDownloadAudio(unittest.TestCase):
    """Test the download_audio function"""

    def setUp(self) -> None:
        self.url = 'https://youtu.be/qpCNaRkIh2E'
        self.yt = pytube.YouTube(self.url)
        return super().setUp()

    def test_download_audio_input_param(self):
        """Validate download_audio url input parameter is a str"""

        with self.assertRaises(TypeError):
            download_audio(1)

    def test_download_audio_file(self):
        """Validate the downloaded file exists"""


# Run unittest as the main module
if __name__ == '__main__':
    unittest.main()
