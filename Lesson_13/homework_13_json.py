import json
import logging
from pathlib import Path

logger = logging.getLogger('JSONValidator')
logger.setLevel(logging.ERROR)
file_handler = logging.FileHandler('/Users/serhii.ravliuk/PycharmProjects/Lesson_2_1/Lesson_13/json_Ravliuk.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def is_valid_json(file_path):
    try:
        with file_path.open('r') as file:
            json.load(file)
        return True
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f'Error reading {file_path}: {e}')
        return False
def validate_json_files(directory, file_names):
    dir_path = Path(directory)

    for file_name in file_names:
        file_path = dir_path / file_name
        if file_path.exists():
            if not is_valid_json(file_path):
                logger.error(f'Invalid JSON file: {file_path}')
        else:
            logger.error(f'File not found: {file_path}')

directory = '/Users/serhii.ravliuk/PycharmProjects/Lesson_2_1/Lesson_13'
files_to_check = [
    'localizations_en.json',
    'localizations_ru.json',
    'login.json',
    'swagger.json'
]
validate_json_files(directory, files_to_check)
