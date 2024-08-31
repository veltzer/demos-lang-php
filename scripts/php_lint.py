#!/usr/bin/env python

"""
A wrapper for the hard to configure "php -l" command line
It turns out this command line emits a line like
""
It also does not allow to treat warnings as errors.
"""

import os.path
import sys
import subprocess

BULLSHIT="bullshit"


def main():
    """ main entry point """
    if len(sys.argv)!=2:
        cmd = sys.argv[0]
        print(f"{cmd}: usage: {cmd} [filename]", file=sys.stderr)
        sys.exit(1)
    filename = sys.argv[1]
    if not os.path.exists(filename):
        print(f"{cmd}: error: file not found: {filename}")
        sys.exit(1)
    result = subprocess.run(
        ["php","-l",filename],
        capture_output=True,
        text=True,
        check=False
    )
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        sys.exit(1)
    lines = []
    for line in result.stdout.split('\n') + result.stderr.split('\n'):
        if line != f"No syntax errors detected in {filename}" and line != "":
            lines.append(line)
    if lines:
        print("\n".join(lines), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
