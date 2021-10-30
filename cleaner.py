# small script that deletes unused graphic files in a latex project.
# specify graphic directory and logfile. Unused files will be deleted in specified directory.

import os
import sys

if __name__ == '__main__':
    enc = 'utf-8' # For Overleaf, try 'Latin-1' if issues encountered...
    directory = 'src'
    logfile = 'output.log'

    try:
        assert len(sys.argv) > 2, 'Missing image folders or .log flie'
        directory = sys.argv[1]
        logfile = sys.argv[2]
    except:
        print(f'Image folder: {directory}, Log file: {logfile}')

    for path, subdirs, files in os.walk(directory):
        for name in files:
            # print(os.path.join(path, name))
            filename = os.path.join(path, name)
            if filename in open(logfile, encoding=enc).read():
                print(filename + ' in use.')
            else:
                if os.path.isfile(filename):
                    print(filename + ' not in use - deleting.')
                    os.remove(os.path.join(filename))
