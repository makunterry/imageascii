#!/usr/bin/env python

import Image
import sys
import os

def log(str):
    pass
    #print("Debug ==> " + str)

def main(args):
    for filename in args:
       if os.path.exists(filename):
	   print("===============================%s============================\n" % filename)
           convert(filename)
	   print("===============================End============================\n")
       else:
           print("File %s did not exist!\n" % filename)

def convert(filename):
    m = [" ", ".", "-", ";", "+", "*", "@", "#"]
    log(filename)
    img_orig = Image.open(filename)

    img = img_orig
    if img_orig.mode != "L":
        img=img_orig.convert("L")
	img_orig.close()

    w,h = img.size
    log("resolution: %d x %d" % (w,h))
    
    ret = ""
    for j in range(0,h,int(h/52.0)):
        for i in range(0,w,int(w/100.0)):
            pixel = img.getpixel((i,j))
    	    ret += m[pixel>>5]
        ret += "\n"
    
    img.close()
    print(ret)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: test.py file1 [ file2 [ ... ] ]")
    else:
        main(sys.argv[1:])
