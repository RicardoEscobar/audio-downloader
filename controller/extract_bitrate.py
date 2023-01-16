def extract_bitrate(bitrate: str) -> str:
    """Extract the bitrate of a string in the form '160kbps' to '160k'.
    This is used to clean the bitrate value to be used on convertion fuinctions.

    Parameters:
    bitrate (str): string containing the bitrate value and the units (kbps)

    Returns:
        str: cleaned bitrate value in the form '160k'"""
    return bitrate.rstrip('bps')
