"""
Check Tags vs. Categories in content/blog
"""
from collections import Counter
from pathlib import Path
import re

counts = Counter()
source = Path.cwd() / "content" / "blog"
for entry in sorted(source.glob("**/*.rst")):
    tags = []
    category = None
    for line in entry.read_text().splitlines():
        if tag_line := re.match(r"^:tags: (.*)?$", line):
            tags = {t.lower() for t in tag_line.group(1).strip().split(',')}
        if cat_line := re.match(r"^:category: (.*)?$", line):
            category = cat_line.group(1).strip()
    if category.lower() in tags:
        print(entry.relative_to(source), category, tags)
        counts[entry.parent.parent.name, entry.parent.name] += 1
# for year, cleanup in counts.items():
#     print(year, cleanup)
