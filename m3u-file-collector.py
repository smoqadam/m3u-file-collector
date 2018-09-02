from __future__ import print_function
from itertools import count
import shutil
import os
import sys
import urllib


try :
    m3ufile = sys.argv.pop(1)
except IndexError :
    print("No m3u file given",file=sys.stderr)
    sys.exit(1)


#check for destination arg
try :
    dest = sys.argv.pop(1)
except IndexError :
    dest = '.'
else :
    os.makedirs(dest)

files = []     



try :
    with open(m3ufile) as f:
        for line in f :
                line = line.strip()
                if line and line[0] != '#' :
                    files.append(urllib.unquote(line).decode('utf8'))
except IOError :
    print ("File not found.")
    sys.exit(1)
    
progress, goal = count(1), len(files)
skipped = []
for path in files:
    # Esc [2J is the VT100 sequence to erase the screen and move the cursor to
    # the beginning of the line
    if os.path.exists(path):
        shutil.copy(path, dest)
        print("\x1b[2J{0} of {1} collected!!".format(next(progress), goal))
    else:
        skipped.append(path)

if skipped:
    print("Missing files:", file=sys.stderr)
    for path in skipped:
        print(path, file=sys.stderr)
    sys.exit(2)
else:
    print("All files collected in {0} directory.  Enjoy!".format(dest))

