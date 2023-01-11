"""
Locate the minimal change set in the content directory when compared
with one of the output directories.

(either the output or the parent directory)

Note that the output directories are defined in the ``Makefile``.
This application is run by make, and executes a series of
``pelicon`` steps.

1. Examine output. Compare with input(s) to see what needs
to be rebuilt.

2. Execute the following to rebuild.

::

    pelican --write-selected output/posts/my-post-title.html

TODO: Better integration with Pelican.
"""

from pathlib import Path
from argparse import Namespace
import re

def meta_dict(entry: Path) -> dict[str, str]:
    meta_pat = re.compile("^:(?P<name>\w+):\s*(?P<value>.*)$")
    matches = filter(None, (meta_pat.match(line) for line in entry.read_text.splitlines()))
    meta = {
        match.group('name'): match.group('value') for match in matches
    }
    return meta

def main(options: Namespace) -> None:
    for source_path in (options.inputdir / "blog").glob("**/*.rst"):
        metadata = meta_dict(source_path)
        slug = metadata['slug']
        source_date = source_path.stat().st_mtime
        target_path = (options.outputdir / slug).with_suffix(".html")
        target_date = target_path.stat().st_mtime

        if target_date < source_date:
            print(f"pelican --write-selected {target_path.relative_to(options.outputdir)}")


if __name__ == "__main__()":
    # options = get_options(sys.argv[1:])
    options = Namespace(inputdir=Path("content"), outputdir=Path("output"))
    main(options)

