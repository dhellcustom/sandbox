from __future__ import print_function
import os, sys
from PIL import Image

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + "_temp.jpg"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.save(outfile, "JPEG")
        except IOError:
            print("Error", infile)
