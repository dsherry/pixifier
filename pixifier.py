#!/usr/bin/env python
import PIL.Image as pil
import ImageFilter
import os.path

print "import successful"

kernelSize = 5

path = "motherboard.jpg"

rootpath, filename = os.path.split(path)
picname, ext = os.path.splitext(filename)
img = pil.open(path)
xs,ys = img.size
new_img = img.filter(ImageFilter.MedianFilter(kernelSize))
new_img.save(rootpath + picname + "-new" + ext)
print "done!"

