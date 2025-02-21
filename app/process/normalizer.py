from datetime import datetime

def normalize_data(data:list) -> list[dict]:
    """convert the date data to a more consistent form"""
    for record in data:
        record['published'] = datetime.strptime(record['published'], '%Y-%m-%dT%H:%M:%SZ')

    return data