#!/usr/bin/python3

# Python imports
import argparse
import faulthandler
import traceback
from setproctitle import setproctitle

import tracemalloc
tracemalloc.start()

# Lib imports

# Application imports
from __builtins__ import *
from app import Application



def main(args, unknownargs):
    setproctitle(f'{app_name}')
    Application(args, unknownargs)



if __name__ == "__main__":
    ''' Set process title, get arguments, and create GTK main thread. '''

    parser = argparse.ArgumentParser()
    # Add long and short arguments
    parser.add_argument("--debug", "-d", default="false", help="Do extra console messaging.")
    parser.add_argument("--trace-debug", "-td", default="false", help="Disable saves, ignore IPC lock, do extra console messaging.")
    parser.add_argument("--no-plugins", "-np", default="false", help="Do not load plugins.")

    parser.add_argument("--new-tab", "-nt", default="false", help="Opens a 'New Tab' if a handler is set for it.")
    parser.add_argument("--file", "-f", default="default", help="JUST SOME FILE ARG.")

    # Read arguments (If any...)
    args, unknownargs = parser.parse_known_args()

    try:
        faulthandler.enable()  # For better debug info
        main(args, unknownargs)
    except Exception as e:
        traceback.print_exc()
        quit()