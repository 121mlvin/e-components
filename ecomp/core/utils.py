import json
from django.conf import settings
from django.utils.translation import get_language


def load_components():
    current_language = get_language()

    # Define the path to the JSON file based on the current language
    json_path = settings.BASE_DIR / f'static/ecomp_{current_language}.json'

    # Open and load the JSON file
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data
