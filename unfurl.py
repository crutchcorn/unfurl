#!/usr/bin/env python3
"""Unfurl - Only the best in town

Usage:
  Unfurl [-r | --respect]
  Unfurl <folder>

Options:
  -h --help                  Show this screen.
  -v --version               Show version.
  -r --respect               Respect directory structure.
  <folder>                   Folder to unfurl.                 EG: Drivers

"""

from os import walk
from os import path
from shutil import move
from docopt import docopt

arguments = docopt(__doc__, version='Unfurl 0.1')

start = path.dirname(path.abspath(__file__))
if arguments["<folder>"]:
    start = path.join(start, arguments["<folder>"]) 
for (dirpath, dirname, filename) in walk(start):
    if filename and start != dirpath:
        if arguments["-r"] or arguments["--respect"]:
            filename += dirname
        for file in filename:
            try:
                move(path.join(start, dirpath, file), start)
            except Exception as e:
                print(e)
                pass
        if arguments["-r"] or arguments["--respect"]:
            break