import json
from urllib.parse import urljoin


def open_json_by_path(file_path):
  with open(file_path, 'r') as file:
    return json.load(file)


def write_json_to_path(data, file_path):
  with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)
