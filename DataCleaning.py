def clean_data(data):
    cleaned = []
    for row in data:  # row = ['bitcoin', 97325]
        # если элемент — строка, чистим; если нет — просто добавляем
        cleaned_row = [str(x).strip().lower() if isinstance(x, str) else x for x in row]
        cleaned.append(cleaned_row)
    return cleaned
