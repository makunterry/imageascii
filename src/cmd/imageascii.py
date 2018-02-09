#!/usr/bin/env python

import argparse
import Image
import sys
import os

cmap_txt = ["\n", " ", ".", "-", ";", "+", "*", "@", "#"]
cmap_html = ["<br>", "&ensp;", ".", "-", ";", "+", "*", "@", "#"]

top_bar_template = "=============================== %s ============================"
bottom_bar = "==================================== %%%%%% ================================="

def log(str):
    pass
    #print("Debug ==> " + str)


def convert(file_name, char_map):
    log(file_name)
    img_orig = Image.open(file_name)

    img = img_orig
    if img_orig.mode != "L":
        img=img_orig.convert("L")
    img_orig.close()

    w,h = img.size
    log("resolution: %d x %d" % (w,h))
    
    ret = ""
    for j in range(0,h,max(1, int(h/52.0))):
        for i in range(0,w,max(1, int(w/110.0))):
            pixel = img.getpixel((i,j))
            ret += char_map[1 + (pixel>>5)]
        ret += char_map[0]
    
    img.close()
    return ret


def handleArgs(args):
    try:
        char_map = cmap_txt
        content = "" # ascii string content
        top_bar = top_bar_template % args.image_file

        if args.html_file:
            char_map = cmap_html
            content += '<html><head><style type="text/css">body {background-color:black;color:white}</style></head><div><h3>' + top_bar + "</h3><tt>"
        else:
            content += top_bar + "\n"

        content += convert(args.image_file, char_map)

        if args.html_file:
            content += "</tt><h3>" + bottom_bar + "</h3></body></html>"
            with open(args.html_file, 'w') as fh:
                fh.write(content)
            print("Image %s converted into html file: %s" % ( args.image_file, args.html_file))
        else:
            content += bottom_bar + "\n"
            print(content)

    except Exception as e:
        print("Error: %s" % e)
        raise e


def main():
    parser = argparse.ArgumentParser(
                description="Simple tool for converting image to ascii"
             )
    parser.add_argument("-H", "--html",
                        metavar="HtmlFile",
                        dest="html_file",
                        help="Store acsii image to HTML file")

    parser.add_argument("image_file",
                        metavar="ImageFile",
                        help="Image file to convert")

    args = parser.parse_args()
    handleArgs(args)
