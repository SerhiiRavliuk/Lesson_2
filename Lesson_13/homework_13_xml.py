import xml.etree.ElementTree as ET
import logging
from pathlib import Path

logger = logging.getLogger('XMLValueLogger')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('/Users/serhii.ravliuk/PycharmProjects/Lesson_2_1/Lesson_13/xml_value_logger.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
def get_incoming_value(group_number, xml_path):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        for group in root.findall('group'):
            number = group.find('number').text
            if number == str(group_number):
                timing_exbytes = group.find('timingExbytes')
                if timing_exbytes is not None:
                    incoming = timing_exbytes.find('incoming')
                    if incoming is not None:
                        return incoming.text
        return None

    except ET.ParseError as e:
        logger.error(f'XML Parse Error: {e}')
        return None
    except Exception as e:
        logger.error(f'Unexpected Error: {e}')
        return None

groups_file_path = '/Users/serhii.ravliuk/PycharmProjects/Lesson_2_1/Lesson_13/groups.xml'

incoming_value = get_incoming_value(2, groups_file_path)

if incoming_value:
    logger.info(f'Incoming value for group number 2: {incoming_value}')
else:
    logger.info('No incoming value found or group number does not exist.')
