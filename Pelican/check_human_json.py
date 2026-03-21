"""
Check content of content/media/human.json
"""
import json
from pathlib import Path
import urllib.request
import sys

from jsonschema import Draft202012Validator

schema_URL = "https://codeberg.org/robida/human.json/raw/branch/main/schema/0.1.1.json"
content_path = Path.cwd() / "content"
human_json_path = content_path / "media" / "human.json"

# 1. Schema
with urllib.request.urlopen(schema_URL) as schema_file:
    schema = json.load(schema_file)
validator = Draft202012Validator(schema)

# 2. Instance (which may not even parse!)
human_json = json.loads(human_json_path.read_text())

# 3. Problems
validator.validate(human_json)

print(f"{human_json_path.relative_to(Path.cwd())} is valid")

