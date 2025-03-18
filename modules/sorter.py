def sort_data(data, criteria):
    # ...existing code...
    if criteria == "name":
        return sorted(data, key=lambda x: x["name"])
    elif criteria == "size":
        return sorted(data, key=lambda x: x["size"])
    elif criteria == "date":
        return sorted(data, key=lambda x: x["modified_time"])
    else:
        raise ValueError("Invalid sorting criteria")
