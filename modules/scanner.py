import os

def scan_library(directory):
    # ...existing code...
    data = []
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            file_info = {
                "name": file,
                "path": filepath,
                "size": os.path.getsize(filepath),
                "modified_time": os.path.getmtime(filepath)
            }
            data.append(file_info)
    return data
