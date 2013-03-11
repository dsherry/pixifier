#!/usr/bin/env python
import PIL.Image as pil
import ImageFilter
from os.path import split, splitext, exists
from math import floor

# user inputs
path = "motherboard.jpg"
block_size = 15 # note: will eventually be "scaling factor" (inverse of block_size)

# internal script settings
# TODO(dylan) unclear what this means for aliasing, more research required
method = pil.NEAREST
# suffix of new file name
new_suffix = "-pixified"
valid_exts = [".jpg"]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

assert exists(path), "Error: no file found at " + path

root_path, filename = split(path)
picname, ext = splitext(filename)
assert ext in valid_exts, "Error: extension %s not in known viable extensions %s \n\
Consult the doc at http://www.pythonware.com/library/pil/handbook/" % (ext, str(valid_exts))
print "Reading %s of type %s from %s" % (filename, ext[1:], ("." if path == "" else path))

img = pil.open(path)
xs,ys = img.size
print "Ingested image of size %spx by %spx" % (xs, ys)

new_xs = int(floor(float(xs)/block_size))
new_ys = int(floor(float(ys)/block_size))
print "Resizing to %spx by %spx" % (new_xs, new_ys)
small_img = img.resize((new_xs,new_ys), method)

print "Scaling back to %spx by %spx" % (xs, ys)
new_img = small_img.resize((xs,ys), method)


new_path = root_path + picname + new_suffix + ext
new_img.save(new_path)
print "New image saved to " + new_path
print "Done! Happy knitting"

