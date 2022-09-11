import os, sys
from stat import *


def walktree(top, callback):
    """recursively descend the directory tree rooted at top,
    calling the callback function for each regular file"""

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.lstat(pathname).st_mode
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname, callback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
            callback(pathname)
        else:
            # Unknown file type, print a message
            print("Skipping %s" % pathname)


def visitfile(file):
    print("visiting", file)


if __name__ == "__main__":
    dir_path = sys.argv[1] if len(sys.argv) == 2 else r"."
    walktree(dir_path, visitfile)
