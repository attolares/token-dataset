import cv2
import glob,os
import os, subprocess
import ntpath

pdf_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(pdf_dir)

i=0

for jpg_file in glob.glob(os.path.join(pdf_dir, "*.jpg")):
    base = ntpath.basename(jpg_file)
    print (base)

    os.system("tesseract "+base+" out"+str(i))
    i = i+1