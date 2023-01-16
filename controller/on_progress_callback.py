def on_progress_callback(stream, chunk, bytes_remaining) -> None:
    """Callback function when there is progress"""
    total_bytes = stream.filesize
    completed_bytes = total_bytes - bytes_remaining
    percentage_completed = (completed_bytes / total_bytes) * 100

    print(f"""Progress = {percentage_completed:.2f}%""")
