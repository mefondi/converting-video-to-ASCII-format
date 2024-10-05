import os
import sys
import shutil
import colorama
import transformations

from PIL import Image
from colorama import Cursor

def main():
    colorama.init()
    print("видео обрабатывается")
    transformations.ToClip(transformations.select_file())
    folder_path = 'extracted_frames'
    file_count = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
    for i in range(file_count):
        with Image.open(f"extracted_frames\{i}.jpg") as im:
            transformations.ToGrayscale(transformations.resize(im))
            sys.stdout.write(Cursor.POS(0, 0)) 
    shutil.rmtree(folder_path)
    
try:
  main()
except:
  shutil.rmtree('extracted_frames') 
