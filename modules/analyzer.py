def analyze_data(data):
    # ...existing code...
    total_files = len(data)
    total_size = sum(item["size"] for item in data)
    return {
        "total_files": total_files,
        "total_size": total_size,
        "average_size": total_size / total_files if total_files > 0 else 0
    }
