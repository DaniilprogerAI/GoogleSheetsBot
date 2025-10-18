def clean_data(data):
    cleaned = []
    for d in data:
        d = d.strip().lower()
        if d not in cleaned and len(d) > 3:
            cleaned.append(d)
    return cleaned
